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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class RestoreDatabaseFromFileRequest(JDCloudRequest):
    """
    从用户上传的备份文件中恢复SQL Server数据库
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(RestoreDatabaseFromFileRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/databases/{dbName}:restoreDatabaseFromFile', 'POST', header, version)
        self.parameters = parameters


class RestoreDatabaseFromFileParameters(object):

    def __init__(self, regionId, instanceId, dbName, fileName):
        """
        :param regionId: 区域代码
        :param instanceId: 实例ID
        :param dbName: 库名称
        :param fileName: 用户在单库上云中上传的文件名称
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.dbName = dbName
        self.sharedFileGid = None
        self.fileName = fileName

    def setSharedFileGid(self, sharedFileGid):
        """
        :param sharedFileGid: (Optional) 共享文件的全局ID，可从上传文件查询接口describeImportFiles获取；如果该文件不是共享文件，则全局ID为空
        """
        self.sharedFileGid = sharedFileGid

