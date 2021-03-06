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


class RestoreDiskRequest(JDCloudRequest):
    """
    从已有快照恢复一块云硬盘
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(RestoreDiskRequest, self).__init__(
            '/regions/{regionId}/disks/{diskId}:restore', 'POST', header, version)
        self.parameters = parameters


class RestoreDiskParameters(object):

    def __init__(self, regionId, diskId, snapshotId):
        """
        :param regionId: 地域ID
        :param diskId: 云硬盘ID
        :param snapshotId: 用于恢复云盘的快照ID
        """

        self.regionId = regionId
        self.diskId = diskId
        self.snapshotId = snapshotId

