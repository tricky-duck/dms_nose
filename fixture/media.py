# -*- coding: utf-8 -*-
from time import sleep
import re
import pyautogui
import pyperclip
import random
from model.media import Media
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class MediaHelper:
    def __init__(self, app):
        self.app = app

    def media_add_one_file_browse(self, media):
        wd = self.app.wd
        alert = self.app.alert
        self.open_media_page()
        wd.find_element_by_xpath('//*[@id="toolbar_controls"]/div/div[1]/button[1]').click()
        sleep(1)
        self.pyautogui_add_one_file(media.file_path)
        wd.find_element_by_xpath('//*[@id="toolbar_controls"]/div/div[1]/button[1]').click()
        alert_text = alert.get_media_message_text()
        self.return_to_media_page()
        self.media_cache = None
        return alert_text

    def media_add_one_file_with_rename(self, media):
        wd = self.app.wd
        alert = self.app.alert
        self.open_media_page()
        wd.find_element_by_xpath('//*[@id="toolbar_controls"]/div/div[1]/button[1]').click()
        sleep(1)
        self.pyautogui_add_one_file(media.file_path)
        wd.find_element_by_xpath('//*[@id="name_copy"]').clear()
        wd.find_element_by_xpath('//*[@id="name_copy"]').send_keys(media.name)
        wd.find_element_by_xpath('//*[@id="toolbar_controls"]/div/div[1]/button[1]').click()
        alert_text = alert.get_media_message_text()
        self.return_to_media_page()
        self.media_cache = None
        return alert_text

    def media_cancel_add_one_file_browse(self, media):
        wd = self.app.wd
        alert = self.app.alert
        self.open_media_page()
        wd.find_element_by_xpath('//*[@id="toolbar_controls"]/div/div[1]/button[1]').click()
        sleep(1)
        self.pyautogui_add_one_file(media.file_path)
        wd.find_element_by_xpath('//*[@id="toolbar_controls"]/div/div[1]/button[2]').click()
        visible = alert.is_visible('//*[@id="msg"]/div/div')
        self.media_cache = None
        return visible

    def media_cancel_add_file_browse_pyauto(self):
        wd = self.app.wd
        alert = self.app.alert
        self.open_media_page()
        wd.find_element_by_xpath('//*[@id="toolbar_controls"]/div/div[1]/button[1]').click()
        sleep(1)
        pyautogui.press('esc')
        visible = alert.is_visible('//*[@id="msg"]/div/div')
        self.media_cache = None
        return visible

    def open_media_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/upload') and len(wd.find_elements_by_link_text('Media Library')) > 0):
            wd.find_element_by_link_text('Media Library').click()

    def return_to_media_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text('Media Library').click()

    @staticmethod
    def pyautogui_add_one_file(full_path):
        if full_path:
            pyperclip.copy(full_path)
            pyautogui.press('down')

            i = 1
            while i < 9:
                i += 1
                pyautogui.press('tab')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            pyautogui.press('enter')

    media_cache = None

    def media_get_list(self):
        if self.media_cache is None:
            wd = self.app.wd
            self.open_media_page()
            self.media_cache = []
            for element in wd.find_elements_by_xpath('//*[@class="gallery"]/*'):
                text_arr = element.text.split('\n')
                name = text_arr[1]
                size = text_arr[0].split(u'×')
                width = size[0]
                height = size[1]
                id = element.get_attribute("data-id")
                self.media_cache.append(Media(name=name, id=id, width=width, height=height))
        return list(self.media_cache)

    def media_get_results_of_search_by_text(self, text):
        if self.media_cache is None:
            wd = self.app.wd
            self.open_media_page()
            self.media_cache = []
            for element in wd.find_elements_by_xpath('//*[@class="gallery"]/*'):
                text_arr = element.text.split('\n')
                name = text_arr[1]
                size = text_arr[0].split(u'×')
                width = size[0]
                height = size[1]
                id = element.get_attribute("data-id")
                self.media_cache.append(Media(name=name, id=id, width=width, height=height))
        return list(self.media_cache)

    def media_search_by_name(self, name):
        wd = self.app.wd
        self.open_media_page()
        search_input = wd.find_element_by_xpath('//*[@id="toolbar_controls"]/div/div[3]/div/input')
        search_input.clear()
        search_input.send_keys(name)
        search_input.send_keys(Keys.RETURN)
        media_list = self.media_get_list()
        self.return_to_media_page()
        self.media_cache = None
        return media_list

    def media_delete_one_file_random_without_select(self):
        wd = self.app.wd
        alert = self.app.alert
        wrapper = self.app.wrapper
        alert_text = []
        self.open_media_page()
        select = self.media_select_random_elements(1)
        self.media_move_to_element_by_name(select[0].name)
        wd.find_element_by_xpath('//*[@title="%s"]/following-sibling::div' % select[0].name).click()
        wrapper.click_if_visible('//*[@id="Dialog-small"]/div/div[2]/div[2]/button[1]')
        alert_text.append(select[0])
        alert_text.append(alert.get_media_message_text())
        self.return_to_media_page()
        self.media_cache = None
        return alert_text

    def media_delete_one_file_by_name_without_select(self, media):
        wd = self.app.wd
        alert = self.app.alert
        wrapper = self.app.wrapper
        self.open_media_page()
        self.media_move_to_element_by_name(media.name)
        wd.find_element_by_xpath('//*[@title="%s"]/following-sibling::div' % media.name).click()
        wrapper.click_if_visible('//*[@id="Dialog-small"]/div/div[2]/div[2]/button[1]')
        alert_text = alert.get_media_message_text()
        self.return_to_media_page()
        self.media_cache = None
        return alert_text

    def media_cancel_delete_one_file_without_select(self, media):
        wd = self.app.wd
        alert = self.app.alert
        self.open_media_page()
        self.media_move_to_element_by_name(media.name)
        wd.find_element_by_xpath('//*[@title="%s"]/following-sibling::div' % media.name).click()
        if alert.is_visible('//*[@id="Dialog-small"]/div/div[2]/div[2]/button[2]'):
            wd.find_element_by_xpath('//*[@id="Dialog-small"]/div/div[2]/div[2]/button[2]').click()
        visible = alert.is_visible('//*[@id="msg"]/div/div')
        self.media_cache = None
        return visible

    def media_delete_number_of_files_with_random_select(self, number):
        wd = self.app.wd
        alert = self.app.alert
        alert_text = []
        self.open_media_page()
        alert_text.append(self.media_select_random_elements(number))
        if alert.is_visible('//*[@id="control_delete pull-right"]/button'):
            wd.find_element_by_xpath('//*[@id="control_delete pull-right"]/button').click()
        alert_text.append(str(alert.get_media_popup_text()))
        wd.find_element_by_xpath('//*[@id="Dialog-small"]/div/div[2]/div[2]/button[1]').click()
        alert_text.append(str(alert.get_media_message_text()))
        self.return_to_media_page()
        self.media_cache = None
        return alert_text

    def media_cancel_delete_number_of_files_random_select(self, number):
        wd = self.app.wd
        alert = self.app.alert
        self.open_media_page()
        self.media_select_random_elements(number)
        if alert.is_visible('//*[@id="control_delete pull-right"]/button'):
            wd.find_element_by_xpath('//*[@id="control_delete pull-right"]/button').click()
        if alert.is_visible('//*[@id="Dialog-small"]/div/div[2]/div[2]/button[2]'):
            wd.find_element_by_xpath('//*[@id="Dialog-small"]/div/div[2]/div[2]/button[2]').click()
        visible = alert.is_visible('//*[@id="msg"]/div/div')
        self.media_cache = None
        return visible

    def media_delete_all_files(self, number):
        wd = self.app.wd
        alert = self.app.alert
        alert_text = []
        self.open_media_page()
        self.media_select_random_elements(number)
        if alert.is_visible('//*[@id="control_delete pull-right"]/button') and \
                alert.is_visible('//*[@id="toolbar_controls"]/div/button'):
            wd.find_element_by_xpath('//*[@id="toolbar_controls"]/div/button').click()
            wd.find_element_by_xpath('//*[@id="control_delete pull-right"]/button').click()
        alert_text.append(str(alert.get_media_popup_text()))
        wd.find_element_by_xpath('//*[@id="Dialog-small"]/div/div[2]/div[2]/button[1]').click()
        alert_text.append(str(alert.get_media_message_text()))
        self.return_to_media_page()
        self.media_cache = None
        return alert_text

    def media_cancel_delete_all_files(self, number):
        wd = self.app.wd
        alert = self.app.alert
        self.open_media_page()
        self.media_select_random_elements(number)
        if alert.is_visible('//*[@id="control_delete pull-right"]/button') and \
                alert.is_visible('//*[@id="toolbar_controls"]/div/button'):
            wd.find_element_by_xpath('//*[@id="toolbar_controls"]/div/button').click()
            wd.find_element_by_xpath('//*[@id="control_delete pull-right"]/button').click()
        if alert.is_visible('//*[@id="Dialog-small"]/div/div[2]/div[2]/button[2]'):
            wd.find_element_by_xpath('//*[@id="Dialog-small"]/div/div[2]/div[2]/button[2]').click()
        visible = alert.is_visible('//*[@id="msg"]/div/div')
        wd.find_element_by_xpath('//*[@id="toolbar_controls"]/div/button').click()
        self.media_cache = None
        return visible

    def media_move_to_element_by_name(self, name):
        wd = self.app.wd
        element = wd.find_element_by_xpath('//*[@title="%s"]' % name)
        mov = ActionChains(wd).move_to_element(element)
        mov.perform()

    def media_select_element_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@title="%s"]' % name).click()

    def media_select_random_elements(self, number):
        media_list = self.media_get_list()
        media_select = []
        for x in range(0, number):
            media_select.append(random.choice(media_list))
            self.media_select_element_by_name(media_select[x].name)
        return media_select

    # выявляем есть ли уже в списке медиа с заданным именем
    # если есть, ищем максимальный индекс по маске "<имя><пробел>(<число>)"
    # переименовывае имя текущей медиа, увеличивая число на 1
    @staticmethod
    def media_get_unique_name(media_name, media_list):
        new_name = media_name
        new_number = 0
        for obj in media_list:
            search_pattern = '%s(\s\(\d+\))?$' % media_name
            if re.match(search_pattern, obj.name) is not None:
                replace_pattern = '\(\d+\)$'
                if re.search(replace_pattern, obj.name) is not None:
                    obj_number = int(re.search(replace_pattern, obj.name).group(0)[1:-1])
                    if not new_number > obj_number:
                        new_number = obj_number + 1
                        new_name = re.sub(replace_pattern, ('(%s)' % str(new_number)), new_name)
                else:
                    new_name += ' (1)'
        return new_name
