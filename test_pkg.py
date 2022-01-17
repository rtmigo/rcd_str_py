from chkpkg import Package

if __name__ == "__main__":
    with Package() as pkg:
        pkg.run_python_code('import rcd_str')

    print("\nPackage is OK!")
