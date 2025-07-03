from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl

# 設定
VCENTER_HOST = '10.85.253.65'
USERNAME = 'Administrator@vsphere.local'
PASSWORD = 'Nttntt123['
NEW_VM_NAME = 'cloned-vm-from-template'
TARGET_FOLDER_NAME = 'vm'
TARGET_DATACENTER_NAME = 'Datacenter'
TARGET_RESOURCE_POOL_NAME = 'Resources'

# SSL無効化（自己署名証明書対応）
context = ssl._create_unverified_context()

# vCenterへ接続
si = SmartConnect(host=VCENTER_HOST, user=USERNAME, pwd=PASSWORD, sslContext=context)
content = si.RetrieveContent()

# 5-4: テンプレートの取得
print("テンプレート一覧:")
template_vm = None
for vm in content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True).view:
    if vm.config.template:
        print(f"- {vm.name}")
        
# 切断
Disconnect(si)