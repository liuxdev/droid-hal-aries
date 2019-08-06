# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device aries
%define vendor xiaomi

%define vendor_pretty XIAOMI
%define device_pretty Mi2S

%define installable_zip 1

%define enable_kernel_update 1

%define straggler_files \
/init.class_main.sh\
/init.qcom.class_core.sh\
/init.qcom.early_boot.sh\
/init.qcom.sh\
/init.qcom.syspart_fixup.sh\
/init.qcom.usb.sh\
/selinux_version\
/service_contexts\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

