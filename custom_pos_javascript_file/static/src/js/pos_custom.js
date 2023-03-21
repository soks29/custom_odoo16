odoo.define('custom_pos.user_interface', function(require) {
	"User strict";
	Var models = require('point_of_sale.models');
	models.load_fields("product.product", ['qty_available']);
});