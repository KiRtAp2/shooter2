from cx_Freeze import setup, Executable

buildOptions = dict(include_files = ['textures/'])

bdist_msi_options = {
	'add_to_path' : False,
	"upgrade_code": "{69b74cba-43dg-2091-9e94-3afcc9e1ad0c}",
	'initial_target_dir': r'[ProgramFilesFolder]\shooter2',
}

setup(
	name="Shooter",
	version="2.1",
	description="Shooter V2.1! Now with powerups which enhance your lonelyness",
	author="KiRtApSquared",
	options=dict(build_exe = buildOptions, bdist_msi=bdist_msi_options),
	executables=[Executable(
		"shooter2.py",
		base="Win32GUI", 
		#shortcutName="Shooter2", 
		#shortcutDir="DesktopFolder"
	)],
)