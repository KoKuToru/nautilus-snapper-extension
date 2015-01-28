#!/usr/bin/python
# -*- coding: utf-8 -*-
#Snapper Nautilus Extension
#Luca Béla Palkovics
#https://github.com/KoKuToru/nautilus-snapper-extension.git
import urllib
import os
from datetime import datetime

from gi.repository import Nautilus, GObject, Gtk

def search_path_list(p, r=None):
    if p == "/":
        return []
    a,b = os.path.split(p)
    snap = a + ("/" if a != "/" else "") + ".snapshots"
    path = b
    if r != None:
        path = path + r
    return [[snap, path]] + search_path_list(a, "/" + path)

def get_snapshot_paths(p):
    ori_modifi = datetime.fromtimestamp(os.path.getmtime(str(p))).strftime("%c")
    path_list = search_path_list(p)
    for item in path_list:
        if (os.path.isdir(item[0])):
            res = []
            for folder in os.listdir(item[0]):
                snapper_path = item[0] + "/" + folder + "/snapshot/" + item[1]
                if os.path.isfile(snapper_path):
                    modifi = datetime.fromtimestamp(os.path.getmtime(snapper_path)).strftime("%c")
                    found = False
                    for i in res:
                        if i[1] == modifi:
                            found = True
                            break
                    if not found and modifi != ori_modifi:
                        res = res + [[snapper_path, modifi]]
            if len(res) > 0:
                return res
    return []

class ColumnExtension(GObject.GObject, Nautilus.PropertyPageProvider):
    def __init__(self):
        pass
    
    def get_property_pages(self, files):
        #check if more than 1 files
        if len(files) > 1:
            return
        
        #just 1 file
        file = files[0]

        filename = urllib.unquote(file.get_uri()[7:])

        snapshots = get_snapshot_paths(filename)

        if len(snapshots) < 1:
            return

        self.property_label = Gtk.Label('Snapper')
        self.property_label.show()

        self.hbox = Gtk.HBox(homogeneous=False, spacing=0)
        self.hbox.show()

        self.value_label = Gtk.Label()
        self.hbox.pack_start(self.value_label, False, False, 0)

        sw = Gtk.ScrolledWindow()
        sw.show()

        self.hbox.pack_start(sw, True, True, 0)

        store = Gtk.ListStore(str, str)

        for snap in snapshots:
            store.append([snap[1], snap[0]])

        treeview = Gtk.TreeView(store)
        treeview.set_rules_hint(True)
        self.create_columns(treeview)
        sw.add(treeview)
        treeview.show()

        treeview.connect('row-activated', self.open_file)

        return Nautilus.PropertyPage(name="NautilusPython::snapper",
                                     label=self.property_label, 
                                     page=self.hbox),

    def create_columns(self, treeview):
        rendererText = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Date", rendererText, text=0)
        column.set_sort_column_id(0)    
        treeview.append_column(column)
        
        rendererText = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Path", rendererText, text=1)
        column.set_sort_column_id(1)
        treeview.append_column(column)

    def open_file(self, treeview, path, column):
        model = treeview.get_model()
        iter = model.get_iter(path)
        filename = model.get_value(iter, 1)
        os.system("xdg-open " + urllib.unquote(filename))
        return
