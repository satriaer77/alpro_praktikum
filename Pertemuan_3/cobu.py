import timg

obj = timg.Renderer()                                                                                               
obj.load_image_from_file("indonesia.png")                                                                                
obj.resize(100,40)
obj.render(timg.ASCIIMethod)
