import glob, subprocess, bs4, os
style = """
	background-color: #121212;
	color: #878787;
	font-family: uw-ttyp0, monospace;
	font-size: 13px;
"""
if not os.path.isdir("generated"):
	os.mkdir("generated")
for f in glob.glob("*.1") + glob.glob("*.8"):
	print("Generating " + f + ".html")
	generated = subprocess.check_output(["env", "BROWSER=cat", "man", "-H", "-l", f]).decode("utf-8")
	s = bs4.BeautifulSoup(generated, "html.parser")
	body = s.find("body")
	body.attrs["style"] = style;
	i = 0;
	while True:
		x = list(body.children)[i]
		print(str(x).lower())
		if str(x).lower().startswith('<hr'):
			x.replaceWith(s.new_string(""))
			break
		if not str(x).lower().startswith("<h1"):
			x.replaceWith(s.new_string(""))
		i += 1
	for i in body.find_all("i"):
		u = s.new_tag("span")
		u.attrs["style"] = "text-decoration: underline;"
		u.contents = i.contents
		i.replaceWith(u)
	st = """<style>
	h2 {
		font-size: inherit;
		margin: 0;
	}
	</style>"""
	open("generated/" + f + ".html", "w").write(str(s) + st)
