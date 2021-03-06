# coding=utf8

# Copyright 2018 JDCLOUD.COM
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


class CleanThresholdSpec(object):

    def __init__(self, cleanThresholdBps=None, cleanThresholdPps=None):
        """
        :param cleanThresholdBps: (Optional) 触发清洗的流量速率，单位bps，范围是10000000到300000000
        :param cleanThresholdPps: (Optional) 触发清洗的包速率，单位pps，范围是2000到70000
        """

        self.cleanThresholdBps = cleanThresholdBps
        self.cleanThresholdPps = cleanThresholdPps
