import click

from hrms.setup import after_install as setup


def after_install():
	try:
		print("Setting up Mitra HRMS...")
		setup()

		click.secho("Thank you for installing Mitra HRMS!", fg="green")

	except Exception as e:
		BUG_REPORT_URL = "https://github.com/frappe/hrms/issues/new"
		click.secho(
			"Installation for Mitra HRMS app failed due to an error."
			" Please try re-installing the app or"
			f" report the issue on {BUG_REPORT_URL} if not resolved.",
			fg="bright_red",
		)
		raise e
