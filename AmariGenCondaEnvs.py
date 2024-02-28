import subprocess

class AmariGenCondaEnvs:
    @staticmethod
    def gen_envs_ymls():
        result = subprocess.check_output("conda env list", shell = True, executable = "/bin/bash", stderr = subprocess.STDOUT).decode()
        for line in result.splitlines():
            env = line.split("/")[0].strip()
            if "base" not in env and "#" not in env:
                subprocess.run(f"source  ~/miniconda3/bin/activate {env} && conda activate {env} && conda env export > AmariCondaEnvs/{env}.yml && conda deactivate", shell = True, executable="/bin/bash")
                print(env)
    @staticmethod
    def create_envs(env_filename):
        result = subprocess.check_output(f"conda env create -f {env_filename}", shell = True, executable = "/bin/bash", stderr = subprocess.STDOUT).decode()
        print(result)
        
    @staticmethod
    def remove_all_envs():
        result = subprocess.check_output("conda env list", shell = True, executable = "/bin/bash", stderr = subprocess.STDOUT).decode()
        for line in result.splitlines():
            env = line.split("/")[0].strip()
            if "base" not in env and "#" not in env:
                subprocess.run(f"source  ~/miniconda3/bin/deactivate && conda remove -n {env} --all -y", shell = True, executable="/bin/bash")
                print(env)

#if __name__ == "__main__":
#    AmariGenCondaEnvs.remove_all_envs()
