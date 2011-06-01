#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Crash Tests Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): David Burns
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

from crash_stats_page import CrashStatsHomePage
from crash_stats_page import CrashStatsSearchResults
import pytest
from unittestzero import Assert
xfail = pytest.mark.xfail

class TestSpecificVersions:

    @xfail(reason="Needs to be updated for the new UI") 
    def test_that_selecting_exact_version_doesnt_show_other_versions(self, seleniumsetup):
        self.selenium = seleniumsetup.selenium
        csp = CrashStatsHomePage(self.selenium)

        details = csp.current_details
        if len(details['versions']) > 0:
            csp.select_version(details['versions'][1])
        
        Assert.equal(details['product'] + ' ' + details['versions'][1],csp.right_column_heading)

        try:
            centre_name = csp.centre_column_heading
            Assert.fail(centre_name + ' was shown when it shouldnt be there')
        except Exception, e:
            pass

        try:
            right_name = csp.right_column_heading
            Assert.fail(right_name + ' was shown when it shouldnt be there')
        except Exception, e:
            pass

