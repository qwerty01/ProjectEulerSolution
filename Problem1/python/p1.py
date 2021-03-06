################################################################################
# Copyright (C) 2014 Qwerty01 (qw3rty01@gmail.com, http://github.com/qwerty01) #
#                                                                              #
# This program is free software; you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation; either version 2 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for    #
# more details.                                                                #
#                                                                              #
# You should have received a copy of the GNU General Public License along with #
# this program; if not, write to the Free Software Foundation, Inc.,           #
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.                #
################################################################################

def getSum(factor, max):
	return ((max-1)/factor+1)*factor*((max-1)/factor)/2 #ilovemath, O(1) solution

print getSum(3,1000)+getSum(5,1000)-getSum(15,1000)