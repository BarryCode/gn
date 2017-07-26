// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef BASE_SYS_INFO_H_
#define BASE_SYS_INFO_H_

#include <stddef.h>
#include <stdint.h>

#include <map>
#include <string>

#include "base/base_export.h"
#include "base/files/file_path.h"
#include "base/gtest_prod_util.h"
#include "base/time/time.h"
#include "build/build_config.h"

namespace base {

namespace debug {
FORWARD_DECLARE_TEST(SystemMetricsTest, ParseMeminfo);
}

struct SystemMemoryInfoKB;

class BASE_EXPORT SysInfo {
 public:
  // Return the number of logical processors/cores on the current machine.
  static int NumberOfProcessors();

  // Return the number of bytes of physical memory on the current machine.
  static int64_t AmountOfPhysicalMemory();

  // Return the number of bytes of current available physical memory on the
  // machine.
  // (The amount of memory that can be allocated without any significant
  // impact on the system. It can lead to freeing inactive file-backed
  // and/or speculative file-backed memory).
  static int64_t AmountOfAvailablePhysicalMemory();

  // Return the number of bytes of virtual memory of this process. A return
  // value of zero means that there is no limit on the available virtual
  // memory.
  static int64_t AmountOfVirtualMemory();

  // Return the number of megabytes of physical memory on the current machine.
  static int AmountOfPhysicalMemoryMB() {
    return static_cast<int>(AmountOfPhysicalMemory() / 1024 / 1024);
  }

  // Return the number of megabytes of available virtual memory, or zero if it
  // is unlimited.
  static int AmountOfVirtualMemoryMB() {
    return static_cast<int>(AmountOfVirtualMemory() / 1024 / 1024);
  }

  // Return the available disk space in bytes on the volume containing |path|,
  // or -1 on failure.
  static int64_t AmountOfFreeDiskSpace(const FilePath& path);

  // Return the total disk space in bytes on the volume containing |path|, or -1
  // on failure.
  static int64_t AmountOfTotalDiskSpace(const FilePath& path);

  // Returns system uptime.
  static TimeDelta Uptime();

  // Returns a descriptive string for the current machine model or an empty
  // string if the machine model is unknown or an error occured.
  // e.g. "MacPro1,1" on Mac, "iPhone9,3" on iOS or "Nexus 5" on Android. Only
  // implemented on OS X, iOS, Android, and Chrome OS. This returns an empty
  // string on other platforms.
  static std::string HardwareModelName();

  // Returns the name of the host operating system.
  static std::string OperatingSystemName();

  // Returns the version of the host operating system.
  static std::string OperatingSystemVersion();

  // Retrieves detailed numeric values for the OS version.
  // DON'T USE THIS ON THE MAC OR WINDOWS to determine the current OS release
  // for OS version-specific feature checks and workarounds. If you must use
  // an OS version check instead of a feature check, use the base::mac::IsOS*
  // family from base/mac/mac_util.h, or base::win::GetVersion from
  // base/win/windows_version.h.
  static void OperatingSystemVersionNumbers(int32_t* major_version,
                                            int32_t* minor_version,
                                            int32_t* bugfix_version);

  // Returns the architecture of the running operating system.
  // Exact return value may differ across platforms.
  // e.g. a 32-bit x86 kernel on a 64-bit capable CPU will return "x86",
  //      whereas a x86-64 kernel on the same CPU will return "x86_64"
  static std::string OperatingSystemArchitecture();

  // Avoid using this. Use base/cpu.h to get information about the CPU instead.
  // http://crbug.com/148884
  // Returns the CPU model name of the system. If it can not be figured out,
  // an empty string is returned.
  static std::string CPUModelName();

  // Return the smallest amount of memory (in bytes) which the VM system will
  // allocate.
  static size_t VMAllocationGranularity();

#if defined(OS_CHROMEOS)
  typedef std::map<std::string, std::string> LsbReleaseMap;

  // Returns the contents of /etc/lsb-release as a map.
  static const LsbReleaseMap& GetLsbReleaseMap();

  // If |key| is present in the LsbReleaseMap, sets |value| and returns true.
  static bool GetLsbReleaseValue(const std::string& key, std::string* value);

  // Convenience function for GetLsbReleaseValue("CHROMEOS_RELEASE_BOARD",...).
  // Returns "unknown" if CHROMEOS_RELEASE_BOARD is not set. Otherwise returns
  // the full name of the board. WARNING: the returned value often differs in
  // developer built system compared to devices that use the official version.
  // E.g. for developer built version, the function could return 'glimmer' while
  // for officially used versions it would be like 'glimmer-signed-mp-v4keys'.
  // Use GetStrippedReleaseBoard() function if you need only the short name of
  // the board (would be 'glimmer' in the case described above).
  static std::string GetLsbReleaseBoard();

  // Convenience function for GetLsbReleaseBoard() removing trailing "-signed-*"
  // if present. Returns "unknown" if CHROMEOS_RELEASE_BOARD is not set.
  static std::string GetStrippedReleaseBoard();

  // Returns the creation time of /etc/lsb-release. (Used to get the date and
  // time of the Chrome OS build).
  static Time GetLsbReleaseTime();

  // Returns true when actually running in a Chrome OS environment.
  static bool IsRunningOnChromeOS();

  // Test method to force re-parsing of lsb-release.
  static void SetChromeOSVersionInfoForTest(const std::string& lsb_release,
                                            const Time& lsb_release_time);
#endif  // defined(OS_CHROMEOS)

#if defined(OS_ANDROID)
  // Returns the Android build's codename.
  static std::string GetAndroidBuildCodename();

  // Returns the Android build ID.
  static std::string GetAndroidBuildID();

  static int DalvikHeapSizeMB();
  static int DalvikHeapGrowthLimitMB();
#endif  // defined(OS_ANDROID)

  // Returns true if this is a low-end device.
  // Low-end device refers to devices having a very low amount of total
  // system memory, typically <= 1GB.
  // See also SysUtils.java, method isLowEndDevice.
  static bool IsLowEndDevice();

 private:
  FRIEND_TEST_ALL_PREFIXES(SysInfoTest, AmountOfAvailablePhysicalMemory);
  FRIEND_TEST_ALL_PREFIXES(debug::SystemMetricsTest, ParseMeminfo);

  static int64_t AmountOfPhysicalMemoryImpl();
  static int64_t AmountOfAvailablePhysicalMemoryImpl();

#if defined(OS_LINUX) || defined(OS_ANDROID) || defined(OS_AIX)
  static int64_t AmountOfAvailablePhysicalMemory(
      const SystemMemoryInfoKB& meminfo);
#endif
};

}  // namespace base

#endif  // BASE_SYS_INFO_H_
