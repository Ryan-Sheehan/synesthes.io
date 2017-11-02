var Jimp = require("jimp");

Jimp.read("/vendor/images/MyFace.JPG").then(function (img) {
    img.resize(256, 256);         // resize

    var img_string = getRGB(img);
    console.log(img_string);

}).catch(function (err) {
    console.error(err);
});

function getRGB(image) {

image.scan(0, 0, image.bitmap.width, image.bitmap.height, function (x, y, idx) {
    
    var rgb_codes = [];
    // x, y is the position of this pixel on the image
    // idx is the position start position of this rgba tuple in the bitmap Buffer
    // this is the image

    var red   = this.bitmap.data[ idx + 0 ];
    var green = this.bitmap.data[ idx + 1 ];
    var blue  = this.bitmap.data[ idx + 2 ];

	console.log(red, blue, green);
	current_rgb = ['r','g','b'];
	rgb_codes.push(current_rgb);
    // rgba values run from 0 - 255
});

}