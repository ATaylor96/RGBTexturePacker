from PIL import Image

r = Image.open("Textures\\roughness.tga").convert('RGB')
g = Image.open("Textures\\metallic.tga").convert('RGB')
b = Image.open("Textures\\ao.tga").convert('RGB')
a = Image.open("Textures\\opacity.tga").convert('RGB')
output_path = "Textures\\result.tga"

print(r.size)

if a != "":
    result = Image.merge("RGBA", [r.convert("L"), g.convert("L"), b.convert("L"), a.convert("L")])

else:
    result = Image.merge("RGB", [r.convert("L"), g.convert("L"), b.convert("L")])

result.save(output_path)
