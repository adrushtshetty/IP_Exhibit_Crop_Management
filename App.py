import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
app = Flask(__name__)
model = pickle.load(open('Model.pkl', 'rb'))

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/crop_prediction')
def crop_prediction():
    return render_template("crop_pred.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/fertilizers')
def fertilizers():
    return render_template("fertilizers_shop.html")

@app.route('/fertilizers_2')
def fertilizers1():
    return render_template("fertilizers_shop_2.html")

@app.route('/fertilizers_3')
def fertilizers2():
    return render_template("fertilizers_shop_3.html")

@app.route('/fert1')
def fert():
    return render_template("fert1.html")

@app.route('/fert2')
def fert2():
    return render_template("fert2.html")

@app.route('/fert3')
def fert3():
    return render_template("fert3.html")

@app.route('/fert4')
def fert4():
    return render_template("fert4.html")

@app.route('/fert5')
def fert5():
    return render_template("fert5.html")

@app.route('/fert6')
def fert6():
    return render_template("fert6.html")

@app.route('/fert7')
def fert7():
    return render_template("fert7.html")

@app.route('/fert8')
def fert8():
    return render_template("fert8.html")

@app.route('/fert9')
def fert9():
    return render_template("fert9.html")

@app.route('/fert10')
def fert10():
    return render_template("fert10.html")

@app.route('/fert11')
def fert11():
    return render_template("fert11.html")

@app.route('/fert12')
def fert12():
    return render_template("fert12.html")

@app.route('/fert13')
def fert13():
    return render_template("fert13.html")

@app.route('/fert15')
def fert15():
    return render_template("fert15.html")

@app.route('/fert16')
def fert16():
    return render_template("fert16.html")

@app.route('/fert17')
def fert17():
    return render_template("fert17.html")

@app.route('/fert18')
def fert18():
    return render_template("fert18.html")

@app.route('/fert19')
def fert19():
    return render_template("fert19.html")

@app.route('/shop')
def shop():
    return render_template("shop.html")

@app.route('/mungbeans')
def mung():
    return render_template("mungbeans.html")

@app.route('/muskmelons')
def musk():
    return render_template("muskmelons.html")

@app.route('/oranges')
def orange():
    return render_template("oranges.html")

@app.route('/papayas')
def pap():
    return render_template("papayas.html")

@app.route('/cotton')
def cotton():
    return render_template("cotton.html")

@app.route('/tea')
def tea():
    return render_template("tea.html")

@app.route('/seeds')
def seeds():
    return render_template("seeds_shop.html")

@app.route('/seeds1')
def seeds1():
    return render_template("seeds_shop-1.html")

@app.route('/seeds3')
def seeds3():
    return render_template("seeds_shop-3.html")

@app.route('/mothbeans')
def moth():
    return render_template("mothbeans.html")

@app.route('/lentil')
def lent():
    return render_template("lentil.html")

@app.route('/blackgram')
def black():
    return render_template("blackgram.html")

@app.route('/pomegranate')
def pomo():
    return render_template("pomegranate.html")

@app.route('/banana')
def ban():
    return render_template("banana.html")

@app.route('/mango')
def man():
    return render_template("mango.html")

@app.route('/grapes')
def grap():
    return render_template("grape.html")

@app.route('/watermelon')
def water():
    return render_template("watermelon.html")

@app.route('/apple')
def apple():
    return render_template("apple.html")

@app.route('/coffee')
def coff():
    return render_template("coffee.html")

@app.route('/coconut')
def coc():
    return render_template("coconut.html")

@app.route('/jute')
def jut():
    return render_template("jute.html")

@app.route('/seeds2')
def seed2():
    return render_template("seeds_shop-2.html")

@app.route('/rice')
def rice():
    return render_template("rice.html")

@app.route('/wheat')
def wheat():
    return render_template("wheat.html")

@app.route('/maize')
def maize():
    return render_template("maize.html")

@app.route('/pigeonpeas')
def pigeonpeas():
    return render_template("pigeonpeas.html")

@app.route('/chickpeas')
def chickpeas():
    return render_template("chickpeas.html")

@app.route('/kidneybeans')
def kidneybeans():
    return render_template("kidenybeans.html")

@app.route('/basics-6')
def basc6():
    return render_template("basic-6.html")

@app.route('/basics-7')
def basc7():
    return render_template("basic-7.html")

@app.route('/basics-1')
def basc1():
    return render_template('basic-1.html')

@app.route('/basics-5')
def basc5():
    return render_template('basic-5.html')

@app.route('/basics-4')
def basc4():
    return render_template('basic-4.html')

@app.route('/basics-3')
def basc3():
    return render_template('basic-3.html')

@app.route('/basics-8')
def basc8():
    return render_template("basic-8.html")

@app.route('/basics-9')
def basc9():
    return render_template("basic-9.html")

@app.route('/basics-2')
def basc2():
    return render_template("basic-2.html")

@app.route('/advc-1')
def advc1():
    return render_template("advc1.html")

@app.route('/advc-2')
def advc2():
    return render_template("advc2.html")

@app.route('/advc-3')
def advc3():
    return render_template("advc3.html")

@app.route('/',methods=['POST'])
def mail():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    me = "drdev.maill@gmail.com"
    you=request.form['Mail']
    print(you)
    # you = "adrushtshetty@gmail.com"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Crop Management"
    msg['From'] = me
    msg['To'] = you

    html = """\
    <!DOCTYPE html>

    <html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
    <head>
    <title></title>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
    <style>
    		* {
    			box-sizing: border-box;
    		}

    		body {
    			margin: 0;
    			padding: 0;
    		}

    		a[x-apple-data-detectors] {
    			color: inherit !important;
    			text-decoration: inherit !important;
    		}

    		#MessageViewBody a {
    			color: inherit;
    			text-decoration: none;
    		}

    		p {
    			line-height: inherit
    		}

    		.desktop_hide,
    		.desktop_hide table {
    			mso-hide: all;
    			display: none;
    			max-height: 0px;
    			overflow: hidden;
    		}

    		@media (max-width:670px) {

    			.desktop_hide table.icons-inner,
    			.social_block.desktop_hide .social-table {
    				display: inline-block !important;
    			}

    			.icons-inner {
    				text-align: center;
    			}

    			.icons-inner td {
    				margin: 0 auto;
    			}

    			.image_block img.big,
    			.row-content {
    				width: 100% !important;
    			}

    			.mobile_hide {
    				display: none;
    			}

    			.stack .column {
    				width: 100%;
    				display: block;
    			}

    			.mobile_hide {
    				min-height: 0;
    				max-height: 0;
    				max-width: 0;
    				overflow: hidden;
    				font-size: 0px;
    			}

    			.desktop_hide,
    			.desktop_hide table {
    				display: table !important;
    				max-height: none !important;
    			}

    			.reverse {
    				display: table;
    				width: 100%;
    			}

    			.reverse .column.first {
    				display: table-footer-group !important;
    			}

    			.reverse .column.last {
    				display: table-header-group !important;
    			}

    			.row-3 td.column.first>table,
    			.row-3 td.column.last>table {
    				padding-left: 20px;
    				padding-right: 20px;
    			}

    			.row-3 td.column.first .border,
    			.row-3 td.column.last .border {
    				border-top: 0;
    				border-right: 0px;
    				border-bottom: 0;
    				border-left: 0;
    			}

    			.row-1 .column-1 .block-5.image_block td.pad {
    				padding: 25px 0 0 !important;
    			}
    		}
    	</style>
    </head>
    <body style="background-color: #000000; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
    <table border="0" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000; background-size: auto;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-size: auto; background-color: #000000; color: #000000; width: 650px;" width="650">
    <tbody>
    <tr>
    <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
    <table border="0" cellpadding="0" cellspacing="0" class="image_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="pad" style="padding-bottom:30px;padding-top:10px;width:100%;padding-right:0px;padding-left:0px;">
    <div align="center" class="alignment" style="line-height:10px"><a href="http://www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="Your Logo" src="https://lh3.googleusercontent.com/CJGIIXx1A-fx3fHNi5ttRJ6gtOtxPPn_ECY7kY9_svVVMK9AmmzgZR7IvAvfQKdUrsSwDEftzKOTT0laRWzp06TML07JtL5F-KX6KcHHX3qdCI4dLbAPmRzwisKKSBZJmmjHA5wTeA=w2400" style="display: block; height: auto; border: 0; width: 163px; max-width: 100%;" title="Your Logo" width="163"/></a></div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="heading_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="pad" style="padding-bottom:5px;text-align:center;width:100%;">
    <h1 style="margin: 0; color: #ffffff; direction: ltr; font-family: Helvetica Neue, Helvetica, Arial, sans-serif; font-size: 56px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder">Maximum yield <br/>and soil fertility</span></h1>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="paragraph_block block-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
    <tr>
    <td class="pad" style="padding-bottom:20px;">
    <div style="color:#ffffff;direction:ltr;font-family:Helvetica Neue, Helvetica, Arial, sans-serif;font-size:16px;font-weight:400;letter-spacing:0px;line-height:150%;text-align:center;mso-line-height-alt:24px;">
    <p style="margin: 0;">"Fields are the future"</p>
    </div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="button_block block-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="pad" style="padding-bottom:15px;text-align:center;">
    <div align="center" class="alignment">
    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://ip-exhibit-crop-management.herokuapp.com/about" style="height:51px;width:198px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#ffffff"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#000000; font-family:Arial, sans-serif; font-size:16px"><![endif]--><a href="https://ip-exhibit-crop-management.herokuapp.com/about" style="text-decoration:none;display:inline-block;color:#000000;background-color:#ffffff;border-radius:0px;width:auto;border-top:0px solid transparent;font-weight:400;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:10px;padding-bottom:10px;font-family:Helvetica Neue, Helvetica, Arial, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;" target="_blank"><span style="padding-left:25px;padding-right:25px;font-size:16px;display:inline-block;letter-spacing:normal;"><span dir="ltr" style="word-break: break-word; line-height: 32px;">Know more about us</span></span></a>
    <!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
    </div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="image_block block-5" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="pad" style="padding-top:5px;width:100%;padding-right:0px;padding-left:0px;">
    <div align="center" class="alignment" style="line-height:10px"><img alt="Laptop" class="big" src="https://lh3.googleusercontent.com/j--BsJUJ1_aBvrjXPAdTwWg2CUtAczF8GipLz3Bm1aD1n_nEOOlEOcC5Jd6L3XLqqr-yOgPnhXzYlCua0ve2fL4K-cv9ONVVh0QM1_RIc5ox6DpvcvPkLl_5P88m0_-0C8gRg5YjzQ=w2400" style="display: block; height: auto; border: 0; width: 423px; max-width: 100%;" title="Laptop" width="423"/></div>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-size: auto;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-size: auto; background-color: #000000; border-radius: 0; color: #000000; width: 650px;" width="650">
    <tbody>
    <tr>
    <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 20px; padding-right: 20px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="50%">
    <table border="0" cellpadding="0" cellspacing="0" class="image_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="pad" style="width:100%;padding-right:0px;padding-left:0px;padding-top:5px;padding-bottom:5px;">
    <div align="center" class="alignment" style="line-height:10px"><img alt="Facebook" src="https://lh3.googleusercontent.com/9RmMBEqUKhORrUh7RoH-uidVDivwp2aurYHACj_HhtrALEiM1Sh7Azgeqzs-Yq5LSQV8XRP-SWvPwAmw9ZSYcFabrRIPlu4kpmHctpl3wusCUiG0R7cdbzWwxGKmmoGRWYnVbuI9vg=w2400" style="display: block; height: auto; border: 0; width: 285px; max-width: 100%;" title="Facebook" width="285"/></div>
    </td>
    </tr>
    </table>
    </td>
    <td class="column column-2" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 20px; padding-right: 20px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="50%">
    <table border="0" cellpadding="0" cellspacing="0" class="social_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="pad" style="text-align:left;padding-right:0px;padding-left:0px;padding-top:5px;">
    <div class="alignment" style="text-align:left;">
    <table border="0" cellpadding="0" cellspacing="0" class="social-table" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block;" width="36px">
    <tr>
    <td style="padding:0 4px 0 0;"><a href="https://www.facebook.com/" target="_blank"><img alt="Facebook" height="32" src="https://lh3.googleusercontent.com/_yg3U5l5aTzM5UcU7HxgWkY8yYi7P-niACdBN38nMOmHqv1mtVbtWDwsC-uGLD3KC5I3La9vbLj7XPUBD085VUMdEgJDErsQ50LUV06wr-JhsQ3fo3t9LmqrrLm-zZFSJxRuhTe_kw=s64-p-k" style="display: block; height: auto; border: 0;" title="facebook" width="32"/></a></td>
    </tr>
    </table>
    </div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="heading_block block-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="pad" style="text-align:center;width:100%;">
    <h1 style="margin: 0; color: #ffffff; direction: ltr; font-family: Helvetica Neue, Helvetica, Arial, sans-serif; font-size: 38px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder">Like us on Facebook</span></h1>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="paragraph_block block-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
    <tr>
    <td class="pad" style="padding-bottom:20px;">
    <div style="color:#ffffff;direction:ltr;font-family:Helvetica Neue, Helvetica, Arial, sans-serif;font-size:16px;font-weight:400;letter-spacing:0px;line-height:150%;text-align:left;mso-line-height-alt:24px;"></div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="button_block block-5" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="pad" style="text-align:left;padding-bottom:5px;">
    <div align="left" class="alignment">
    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="http://www.example.com" style="height:51px;width:118px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#ffffff"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#000000; font-family:Arial, sans-serif; font-size:16px"><![endif]--><a href="http://www.example.com" style="text-decoration:none;display:inline-block;color:#000000;background-color:#ffffff;border-radius:0px;width:auto;border-top:0px solid transparent;font-weight:400;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:10px;padding-bottom:10px;font-family:Helvetica Neue, Helvetica, Arial, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;" target="_blank"><span style="padding-left:25px;padding-right:25px;font-size:16px;display:inline-block;letter-spacing:normal;"><span dir="ltr" style="word-break: break-word; line-height: 32px;">Follow us</span></span></a>
    <!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
    </div>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-size: auto;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-size: auto; background-color: #000000; border-radius: 0; color: #000000; width: 650px;" width="650">
    <tbody>
    <tr class="reverse">
    <td class="column column-1 first" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 20px; padding-right: 20px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="50%">
    <div class="border">
    <table border="0" cellpadding="0" cellspacing="0" class="social_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="pad" style="text-align:left;padding-right:0px;padding-left:0px;padding-top:5px;">
    <div class="alignment" style="text-align:left;">
    <table border="0" cellpadding="0" cellspacing="0" class="social-table" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block;" width="36px">
    <tr>
    <td style="padding:0 4px 0 0;"><a href="https://instagram.com/" target="_blank"><img alt="Instagram" height="32" src="https://lh3.googleusercontent.com/-hOBuBdFMC3bQbj9fuKC1dvBSlA54v2TNkd2Pyw2nG8IH3v6Z-764TdCR2LGXTKZa8b5HdkRmwr7HSjYuj4Gcz_VCDkXS3uF50fsnBIgpmP2thNcg3Bs4l8GV8XxR6lbxj69M13SZw=s64-p-k" style="display: block; height: auto; border: 0;" title="Instagram" width="32"/></a></td>
    </tr>
    </table>
    </div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="heading_block block-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="pad" style="text-align:center;width:100%;">
    <h1 style="margin: 0; color: #ffffff; direction: ltr; font-family: Helvetica Neue, Helvetica, Arial, sans-serif; font-size: 38px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder">Follow us on Instagram</span></h1>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="paragraph_block block-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
    <tr>
    <td class="pad" style="padding-bottom:20px;">
    <div style="color:#ffffff;direction:ltr;font-family:Helvetica Neue, Helvetica, Arial, sans-serif;font-size:16px;font-weight:400;letter-spacing:0px;line-height:150%;text-align:left;mso-line-height-alt:24px;"></div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="button_block block-5" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="pad" style="text-align:left;padding-bottom:5px;">
    <div align="left" class="alignment">
    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="http://www.example.com" style="height:51px;width:118px;v-text-anchor:middle;" arcsize="0%" stroke="false" fillcolor="#ffffff"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#000000; font-family:Arial, sans-serif; font-size:16px"><![endif]--><a href="http://www.example.com" style="text-decoration:none;display:inline-block;color:#000000;background-color:#ffffff;border-radius:0px;width:auto;border-top:0px solid transparent;font-weight:400;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:10px;padding-bottom:10px;font-family:Helvetica Neue, Helvetica, Arial, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;" target="_blank"><span style="padding-left:25px;padding-right:25px;font-size:16px;display:inline-block;letter-spacing:normal;"><span dir="ltr" style="word-break: break-word; line-height: 32px;">Follow us</span></span></a>
    <!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
    </div>
    </td>
    </tr>
    </table>
    </div>
    </td>
    <td class="column column-2 last" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 20px; padding-right: 20px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="50%">
    <div class="border">
    <table border="0" cellpadding="0" cellspacing="0" class="image_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="pad" style="width:100%;padding-right:0px;padding-left:0px;padding-top:5px;padding-bottom:5px;">
    <div align="center" class="alignment" style="line-height:10px"><img alt="Instagram" src="https://lh3.googleusercontent.com/8Ux22hJmpmRYrHh1wN-j5YepxJfgJO68uxxv1duWAErnMZi33t78NcKUWMg4DEs7DYmt_x1EENIJfD8VGHRR2Yf5ZG34gnYoRkRAnFgCcapW86HhgsYOOQXN4q4J1T_JWcCYCeiC-A=w2400" style="display: block; height: auto; border: 0; width: 285px; max-width: 100%;" title="Instagram" width="285"/></div>
    </td>
    </tr>
    </table>
    </div>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000; border-radius: 0; color: #000000; width: 650px;" width="650">
    <tbody>
    <tr>
    <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
    <div class="spacer_block" style="height:35px;line-height:35px;font-size:1px;"> </div>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-5" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000; border-radius: 0; color: #000000; width: 650px;" width="650">
    <tbody>
    <tr>
    <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
    <table border="0" cellpadding="0" cellspacing="0" class="social_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="pad" style="text-align:center;padding-right:0px;padding-left:0px;">
    <div class="alignment" style="text-align:center;">
    <table border="0" cellpadding="0" cellspacing="0" class="social-table" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block;" width="72px">
    <tr>
    <td style="padding:0 2px 0 2px;"><a href="https://www.facebook.com/" target="_blank"><img alt="Facebook" height="32" src="https://lh3.googleusercontent.com/_yg3U5l5aTzM5UcU7HxgWkY8yYi7P-niACdBN38nMOmHqv1mtVbtWDwsC-uGLD3KC5I3La9vbLj7XPUBD085VUMdEgJDErsQ50LUV06wr-JhsQ3fo3t9LmqrrLm-zZFSJxRuhTe_kw=s64-p-k" style="display: block; height: auto; border: 0;" title="facebook" width="32"/></a></td>
    <td style="padding:0 2px 0 2px;"><a href="https://www.instagram.com/" target="_blank"><img alt="Instagram" height="32" src="https://lh3.googleusercontent.com/6gFylM_zbMzGvcjM_f7cWOAoYJOiG2jipMxftNtL9du_HHOzLG7rOhWHWkmHTVIYAxmal3BSXml_tGOeIyGrh9m6Ys6iDLzjGRtJadvVvVmryKZAO81k-EZRgc49nXe9kBUJfkBLBg=w2400" style="display: block; height: auto; border: 0;" title="instagram" width="32"/></a></td>
    </tr>
    </table>
    </div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="paragraph_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
    <tr>
    <td class="pad" style="padding-bottom:5px;">
    <div style="color:#ffffff;direction:ltr;font-family:Helvetica Neue, Helvetica, Arial, sans-serif;font-size:16px;font-weight:400;letter-spacing:0px;line-height:150%;text-align:center;mso-line-height-alt:24px;">
    <p style="margin: 0;">2022 © All rights reserved</p>
    </div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="paragraph_block block-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
    <tr>
    <td class="pad" style="padding-bottom:5px;padding-left:20px;padding-right:20px;">
    <div style="color:#ffffff;direction:ltr;font-family:Helvetica Neue, Helvetica, Arial, sans-serif;font-size:12px;font-weight:400;letter-spacing:0px;line-height:180%;text-align:center;mso-line-height-alt:21.6px;">
    <p style="margin: 0;"><a href="http://example.com" rel="noopener" style="text-decoration: none; color: #737172;" target="_blank">Unsuscribe</a></p>
    </div>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-6" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
    <tbody>
    <tr>
    <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
    <table border="0" cellpadding="0" cellspacing="0" class="icons_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="pad" style="vertical-align: middle; color: #9d9d9d; font-family: inherit; font-size: 15px; padding-bottom: 5px; padding-top: 5px; text-align: center;">
    <table cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="alignment" style="vertical-align: middle; text-align: center;">
    <!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
    <!--[if !vml]><!-->
    <table cellpadding="0" cellspacing="0" class="icons-inner" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;">
    <!--<![endif]-->
    <!--<tr>-->
    <!--<td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 6px;"><a href="https://www.designedwithbee.com/" style="text-decoration: none;" target="_blank"><img align="center" alt="Designed with BEE" class="icon" height="32" src="static/img/bee.png" style="display: block; height: auto; margin: 0 auto; border: 0;" width="34"/></a></td>-->
    <!--<td style="font-family: Helvetica Neue, Helvetica, Arial, sans-serif; font-size: 15px; color: #9d9d9d; vertical-align: middle; letter-spacing: undefined; text-align: center;"><a href="https://www.designedwithbee.com/" style="color: #9d9d9d; text-decoration: none;" target="_blank">Designed with BEE</a></td>-->
    <!--</tr>-->
    </table>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table><!-- End -->
    </body>
    </html>
    """
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('drdev.maill@gmail.com', 'mmieeonadmnrylqz')
    mail.sendmail(me, you, msg.as_string())
    mail.quit()

    return render_template("index.html")

@app.route('/crop_prediction',methods=['POST'])
def predict():

    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    if prediction[0] == 20:
        output ="Rice"
    elif prediction[0] == 11:
        output ="Maize"
    elif prediction[0] == 3:
        output ="Chickpeas"
    elif prediction[0] == 9:
        output = "Kidneybeans"
    elif prediction[0] == 18:
        output ="Pigeonpeas"
    elif prediction[0] == 13:
        output ="Mothbeans"
    elif prediction[0] == 14:
        output ="Mungbeans"
    elif prediction[0] == 2:
        output ="Blackgram"
    elif prediction[0] == 10:
        output ="Lentil"
    elif prediction[0] == 19:
        output ="Pomegranate"
    elif prediction[0] == 1:
        output ="Bananas"
    elif prediction[0] == 12:
        output ="Mangoes"
    elif prediction[0] == 7:
        output ="Grapes"
    elif prediction[0] == 21:
        output ="Watermelons"
    elif prediction[0] == 15:
        output ="Muskmelons"
    elif prediction[0] == 0:
        output ="Apples"
    elif prediction[0] == 16:
        output ="Oranges"
    elif prediction[0] == 17:
        output ="Papayas"
    elif prediction[0] == 4:
        output ="Coconuts"
    elif prediction[0] == 6:
        output ="Cotton"
    elif prediction[0] == 8:
        output ="Jute"
    elif prediction[0] == 5:
        output ="Coffee"


    return render_template('crop_pred.html', prediction_text='{}'.format(output),check=output)

@app.route('/crop_requisites_1')
def bench_1():
    return render_template("bench_1.html")
@app.route('/crop_requisites_2')
def bench_2():
    return render_template("bench_2.html")
@app.route('/crop_requisites_3')
def bench_3():
    return render_template("bench_3.html")
if __name__ == '__main__':
    app.run(debug=True)