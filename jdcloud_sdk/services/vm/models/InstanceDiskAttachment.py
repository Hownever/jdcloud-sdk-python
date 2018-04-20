# coding=utf8

# Copyright 2018-2025 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class InstanceDiskAttachment(object):

    def __init__(self, diskCategory=None, autoDelete=None, localDisk=None, cloudDisk=None, deviceName=None):
        """
        :param diskCategory: (Optional) 磁盘分类，取值范围{local, cloud}
        :param autoDelete: (Optional) 自动删除，删除主机时自动删除此磁盘，默认为True
        :param localDisk: (Optional) 本地磁盘
        :param cloudDisk: (Optional) 云硬盘
        :param deviceName: (Optional) 数据盘逻辑挂载点vdb,vdc,vdd,vde,vdf,vdg,vdh
        """

        self.diskCategory = diskCategory
        self.autoDelete = autoDelete
        self.localDisk = localDisk
        self.cloudDisk = cloudDisk
        self.deviceName = deviceName