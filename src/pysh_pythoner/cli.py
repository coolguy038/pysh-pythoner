def main():

	from pathlib import Path

	import tomlkit

	config_path = Path.home() / ".pysh.toml"

	with open(config_path, encoding="utf-8") as f:
		pysh = tomlkit.load(f)

	if "plugins" not in pysh:
		pysh["plugins"] = tomlkit.table()

	pysh["plugins"]["python_as_pythoner"] = (
		"if command == 'python':\n	subprocess.run('pythoner', stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)\n	break"
	)

	with open(config_path, "w", encoding="utf-8") as f:
		tomlkit.dump(pysh, f)
