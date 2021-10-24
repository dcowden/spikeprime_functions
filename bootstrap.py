#make sure to declare this variable
VM = None
STACK = None

def your_startup_code)
  #put your start up code here
  pass

def main(vm, stack):
    global VM,STACK
    VM = vm
    STACK = stack
    print("running vroom")
    try:
        your_startup_code()
    except BaseException as err:
        sys.print_exception(err)
    print ("^^^^^^^^Stopping due to Exception!^^^^^^^")
    vm.stop()

def setup(rpc, system, stop):
    print("Setting Up")
    vm = runtime.VirtualMachine(rpc, system, stop, "1670_code")
    vm.register_on_start("main_on_start", main)
    return vm

class RPC:
    def emit(self, op, id):
        pass

setup(RPC(), system.system, sys.exit).start()
