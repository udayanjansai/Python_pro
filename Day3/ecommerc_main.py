import ecommerce
dic={'phone':30000,'laptop':55000,'tv':2000}
dis=ecommerce.discount(dic,10)
gst=ecommerce.add_gst(dic,18)
ecommerce.invoice(dic,dis,gst)