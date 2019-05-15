import xlwt
import base64
from PIL import Image
from cStringIO import StringIO
from odoo import models, fields, api, _

class xlwt_image(models.TransientModel):
    _name = 'xlwt.image'

    data_file = fields.Binary("File")
    name = fields.Char("Filename")
    pict = fields.Binary("Picture")

    def export_excel(self, vals, context=None):
        # add an excel file, a sheet with overwrite cell, magnifier code #  
        book = xlwt.Workbook()
        sheet = book.add_sheet("Image On Xls", cell_overwrite_ok=True)
        sheet.normal_magn = 80
        # ------------------------------------------------------ #

        # decode uploaded pict as base64 and buffer it with StringIO #
        image_base64 = str(self.pict).decode('base64')
        image_data = StringIO(image_base64)
        # ---------------------------------------------------------- #

        # use these code if want to resize that image #
        # new_img = img.resize((281, 97))
        # new_img.save('/home/odhon/Pictures/pict.bmp')
        # ------------------------------------------- #

        # comment these code if u use the resize code # 
        img = Image.open(image_data).convert('RGB')
        img.save('/home/odhon/Pictures/pict.bmp')
        # ------------------------------------------- #

        # write image on sheet, fill insert_bitmap method with path, row, column, x y point and scale) #
        sheet.insert_bitmap('/home/odhon/Pictures/pict.bmp', 3, 3, x=10, y=10, scale_x=1, scale_y=1)
        # -------------------------------------------------------------------------------------------- #

        # finally save it, write out and return it to xml view # 
        file_data = StringIO()
        book.save(file_data)
        filename = 'Image On Xls.xls'
        out = base64.encodestring(file_data.getvalue())
        self.write({'data_file': out, 'name': filename})
        view_rec = self.env['ir.model.data'].get_object_reference('xlwt_image', 'view_wizard_xlwt_image')
        view_id = view_rec[1] or False
        # ---------------------------------------------------- #

        return {
            'view_type': 'form',
            'view_id': [view_id],
            'view_mode': 'form',
            'res_id': self.id,
            'res_model': 'xlwt.image',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
