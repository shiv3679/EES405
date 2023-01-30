shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ncdump -h air.mon.ltm.nc 
Command 'ncdump' not found, but can be installed with:
sudo apt install netcdf-bin
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ sudo apt install netcdf-bin
[sudo] password for shiv: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  chromium-codecs-ffmpeg-extra gstreamer1.0-vaapi i965-va-driver intel-media-va-driver libaacs0 libaom3 libass9 libavcodec58 libavformat58 libavutil56 libbdplus0 libblas3
  libbluray2 libbs2b0 libchromaprint1 libcodec2-1.0 libdav1d5 libflashrom1 libflite1 libftdi1-2 libgme0 libgsm1 libgstreamer-plugins-bad1.0-0 libigdgmm12 liblilv-0-0
  libmfx1 libmysofa1 libnorm1 libopenmpt0 libpgm-5.3-0 libpostproc55 librabbitmq4 librubberband2 libserd-0-0 libshine3 libsnappy1v5 libsord-0-0 libsratom-0-0
  libsrt1.4-gnutls libssh-gcrypt-4 libswresample3 libswscale5 libudfread0 libva-drm2 libva-wayland2 libva-x11-2 libva2 libvdpau1 libvidstab1.1 libx265-199 libxvidcore4
  libzimg2 libzmq5 libzvbi-common libzvbi0 mesa-va-drivers mesa-vdpau-drivers pocketsphinx-en-us va-driver-all vdpau-driver-all
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  netcdf-bin
0 upgraded, 1 newly installed, 0 to remove and 16 not upgraded.
Need to get 204 kB of archives.
After this operation, 557 kB of additional disk space will be used.
Get:1 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 netcdf-bin amd64 1:4.8.1-1 [204 kB]
Fetched 204 kB in 4s (47.3 kB/s)     
Selecting previously unselected package netcdf-bin.
(Reading database ... 214117 files and directories currently installed.)
Preparing to unpack .../netcdf-bin_1%3a4.8.1-1_amd64.deb ...
Unpacking netcdf-bin (1:4.8.1-1) ...
Setting up netcdf-bin (1:4.8.1-1) ...
Processing triggers for man-db (2.10.2-1) ...
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ncdump -h air.mon.ltm.nc 
netcdf air.mon.ltm {
dimensions:
	lon = 144 ;
	lat = 73 ;
	level = 17 ;
	time = 12 ;
	nbnds = 2 ;
variables:
	float level(level) ;
		level:units = "millibar" ;
		level:actual_range = 1000.f, 10.f ;
		level:long_name = "Level" ;
		level:positive = "down" ;
		level:GRIB_id = 100s ;
		level:GRIB_name = "hPa" ;
		level:axis = "Z" ;
		level:coordinate_defines = "point" ;
	float lat(lat) ;
		lat:units = "degrees_north" ;
		lat:actual_range = 90.f, -90.f ;
		lat:long_name = "Latitude" ;
		lat:standard_name = "latitude" ;
		lat:axis = "Y" ;
		lat:coordinate_defines = "point" ;
	float lon(lon) ;
		lon:units = "degrees_east" ;
		lon:long_name = "Longitude" ;
		lon:actual_range = 0.f, 357.5f ;
		lon:standard_name = "longitude" ;
		lon:axis = "X" ;
		lon:coordinate_defines = "point" ;
	double time(time) ;
		time:units = "hours since 1800-1-1 00:00:00" ;
		time:long_name = "Time" ;
		time:delta_t = "0000-01-00 00:00:00" ;
		time:avg_period = "0030-00-00 00:00:00" ;
		time:prev_avg_period = "0000-01-00 00:00:00" ;
		time:standard_name = "time" ;
		time:axis = "T" ;
		time:coordinate_defines = "start" ;
		time:bounds = "time_bnds" ;
		time:climatology = "climatology_bounds" ;
		time:climo_period = "1991/01/01 - 2020/12/31" ;
		time:actual_range = -15769752., -15761736. ;
		time:ltm_range = 1674264., 1936512. ;
		time:interpreted_actual_range = "0001/01/01 00:00:00 - 0001/12/01 00:00:00" ;
	double climatology_bounds(time, nbnds) ;
		climatology_bounds:long_name = "Climate Time Boundaries" ;
		climatology_bounds:units = "hours since 1800-1-1 00:00:00" ;
	float air(time, level, lat, lon) ;
		air:long_name = "Long Term Mean Monthly Air Temperature on Pressure Levels" ;
		air:units = "degK" ;
		air:precision = 2s ;
		air:least_significant_digit = 1s ;
		air:GRIB_id = 11s ;
		air:GRIB_name = "TMP" ;
		air:var_desc = "Air temperature" ;
		air:dataset = "NCEP/DOE AMIP-II Reanalysis (Reanalysis-2) Monthly Averages" ;
		air:level_desc = "Pressure Levels" ;
		air:statistic = "Long Term Mean" ;
		air:parent_stat = "Individual Obs" ;
		air:standard_name = "air_temperature" ;
		air:cell_methods = "time: mean (monthly from 6-hourly values)" ;
		air:missing_value = -9.96921e+36f ;
		air:valid_range = 137.5f, 362.5f ;
		air:actual_range = 183.0121f, 314.302f ;
	short valid_yr_count(time, level, lat, lon) ;
		valid_yr_count:long_name = "count of non-missing values used in mean" ;
		valid_yr_count:missing_value = 32767s ;
		valid_yr_count:add_offset = 0.f ;
		valid_yr_count:scale_factor = 1.f ;

// global attributes:
		:Conventions = "CF-1.0" ;
		:title = "Monthly NCEP/DOE Reanalysis 2" ;
		:comments = "Data is from \n",
			"NCEP/DOE AMIP-II Reanalysis (Reanalysis-2)\n",
			"(4x/day).  It consists of most variables interpolated to\n",
			"pressure surfaces from model (sigma) surfaces." ;
		:platform = "Model" ;
		:source = "NCEP/DOE AMIP-II Reanalysis (Reanalysis-2) Model" ;
		:institution = "National Centers for Environmental Prediction" ;
		:dataset_title = "NCEP-DOE AMIP-II Reanalysis" ;
		:References = "https://www.psl.noaa.gov/data/gridded/data.ncep.reanalysis2.html" ;
		:source_url = "http://www.cpc.ncep.noaa.gov/products/wesley/reanalysis2/" ;
		:history = "Created 2022/01/11 by doMonthLTMNC4" ;
		:not_missing_threshold_percent = "minimum 3% values input to have non-missing output value" ;
}
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ sudo apt-get install cdo
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  chromium-codecs-ffmpeg-extra gstreamer1.0-vaapi i965-va-driver intel-media-va-driver libaacs0 libaom3 libass9 libavcodec58 libavformat58 libavutil56 libbdplus0 libbluray2 libbs2b0 libchromaprint1
  libcodec2-1.0 libdav1d5 libflashrom1 libflite1 libftdi1-2 libgme0 libgsm1 libgstreamer-plugins-bad1.0-0 libigdgmm12 liblilv-0-0 libmfx1 libmysofa1 libopenmpt0 libpostproc55 librabbitmq4 librubberband2
  libserd-0-0 libshine3 libsord-0-0 libsratom-0-0 libsrt1.4-gnutls libssh-gcrypt-4 libswresample3 libswscale5 libudfread0 libva-drm2 libva-wayland2 libva-x11-2 libva2 libvdpau1 libvidstab1.1 libx265-199
  libxvidcore4 libzimg2 libzvbi-common libzvbi0 mesa-va-drivers mesa-vdpau-drivers pocketsphinx-en-us va-driver-all vdpau-driver-all
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  binfmt-support blt fonts-dejavu-extra fonts-font-awesome fonts-lato fonts-lyx ibverbs-providers icu-devtools libblosc1 libboost-dev libboost1.74-dev libcdi0 libclang-cpp11 libdouble-conversion3 libdxflib3
  libeccodes-data libeccodes0 libeckit0d libevent-core-2.1-7 libevent-pthreads-2.1-7 libfabric1 libffi-dev libfftw3-double3 libfuse2 libgeotiff5 libgit2-1.1 libhttp-parser2.9 libhwloc-plugins libhwloc15
  libibverbs1 libicu-dev libjs-jquery-ui liblbfgsb0 libllvm11 liblzf1 libmagics++-data libmagplus3v5 libmbedcrypto7 libmbedtls14 libmbedx509-1 libmd4c0 libmysqlclient21 libncurses-dev libodc-0d libopenblas-dev
  libopenblas-pthread-dev libopenblas0 libopenblas0-pthread libopenmpi3 libpcre2-16-0 libpfm4 libpmix2 libpq5 libpsm-infinipath1 libpsm2-2 libqhull-r8.0 libqt5core5a libqt5dbus5 libqt5gui5 libqt5network5
  libqt5svg5 libqt5widgets5 librdmacm1 libssh2-1 libtbb12 libtbbmalloc2 libterralib3 libtinfo-dev libucx0 libxcb-xinerama0 libxcb-xinput0 libxml2-dev libxnvctrl0 libxsimd-dev libz3-4 libz3-dev llvm-11
  llvm-11-dev llvm-11-linker-tools llvm-11-runtime llvm-11-tools mysql-common numba-doc python-babel-localedata python-matplotlib-data python-odf-doc python-odf-tools python-tables-data python3-appdirs
  python3-asciitree python3-attr python3-babel python3-beniget python3-blosc python3-bottleneck python3-brotli python3-bs4 python3-cdo python3-cftime python3-cloudpickle python3-cycler python3-dask
  python3-decorator python3-defusedxml python3-distributed python3-dropbox python3-et-xmlfile python3-fonttools python3-fs python3-fsspec python3-fusepy python3-gast python3-h5netcdf python3-h5py-serial
  python3-heapdict python3-html5lib python3-iniconfig python3-jdcal python3-jinja2 python3-kiwisolver python3-libarchive-c python3-llvmlite python3-locket python3-lxml python3-lz4 python3-matplotlib
  python3-mpmath python3-msgpack python3-netcdf4 python3-numba python3-numcodecs python3-numexpr python3-numpy python3-odf python3-openpyxl python3-packaging python3-pandas python3-pandas-lib python3-partd
  python3-pil.imagetk python3-pluggy python3-ply python3-psutil python3-py python3-pygit2 python3-pygments python3-pytest python3-pythran python3-scipy python3-sortedcontainers python3-soupsieve python3-stone
  python3-sympy python3-tables python3-tables-lib python3-tblib python3-tk python3-toml python3-toolz python3-tornado python3-ufolib2 python3-unicodedata2 python3-webencodings python3-xarray python3-xlwt
  python3-zarr python3-zict python3-zmq qt5-gtk-platformtheme qttranslations5-l10n sphinx-rtd-theme-common tk8.6-blt2.5 unicode-data
Suggested packages:
  blt-demo libboost-doc libboost1.74-doc libboost-atomic1.74-dev libboost-chrono1.74-dev libboost-container1.74-dev libboost-context1.74-dev libboost-contract1.74-dev libboost-coroutine1.74-dev
  libboost-date-time1.74-dev libboost-exception1.74-dev libboost-fiber1.74-dev libboost-filesystem1.74-dev libboost-graph1.74-dev libboost-graph-parallel1.74-dev libboost-iostreams1.74-dev
  libboost-locale1.74-dev libboost-log1.74-dev libboost-math1.74-dev libboost-mpi1.74-dev libboost-mpi-python1.74-dev libboost-numpy1.74-dev libboost-program-options1.74-dev libboost-python1.74-dev
  libboost-random1.74-dev libboost-regex1.74-dev libboost-serialization1.74-dev libboost-stacktrace1.74-dev libboost-system1.74-dev libboost-test1.74-dev libboost-thread1.74-dev libboost-timer1.74-dev
  libboost-type-erasure1.74-dev libboost-wave1.74-dev libboost1.74-tools-dev libmpfrc++-dev libntl-dev libboost-nowide1.74-dev libfftw3-bin libfftw3-dev geotiff-bin gdal-bin libgeotiff-epsg
  libhwloc-contrib-plugins icu-doc libjs-jquery-ui-docs ncurses-doc qt5-image-formats-plugins qtwayland5 libterralib-doc pkg-config libxsimd-doc llvm-11-doc python-attr-doc python-blosc-doc
  python-bottleneck-doc python-cycler-doc ipython python-dask-doc python3-bcolz python3-boto python3-graphviz python3-h5py python3-skimage python3-sklearn python3-sqlalchemy python-fsspec-doc python-h5py-doc
  python3-genshi python-jinja2-doc llvmlite-doc python-lxml-doc dvipng ffmpeg fonts-staypuft inkscape ipython3 python-matplotlib-doc python3-cairocffi python3-gobject python3-pyqt5 python3-sip
  texlive-extra-utils texlive-latex-extra python-mpmath-doc python3-gmpy2 nvidia-cuda-toolkit python-numpy-doc python-pandas-doc python3-statsmodels python-pil-doc python-ply-doc python-psutil-doc subversion
  python-pygit2-doc python-pygments-doc ttf-bitstream-vera python-scipy-doc python-sortedcontainers-doc texlive-fonts-extra python-sympy-doc python-tables-doc vitables tix python3-tk-dbg python-toolz-doc
  python3-pycurl python-tornado-doc python3-twisted python-xarray-doc python3-cartopy python3-pydap python3-rasterio python3-seaborn python3-xlrd python-xlrt-doc jupyter-notebook
The following NEW packages will be installed:
  binfmt-support blt cdo fonts-dejavu-extra fonts-font-awesome fonts-lato fonts-lyx ibverbs-providers icu-devtools libblosc1 libboost-dev libboost1.74-dev libcdi0 libclang-cpp11 libdouble-conversion3
  libdxflib3 libeccodes-data libeccodes0 libeckit0d libevent-core-2.1-7 libevent-pthreads-2.1-7 libfabric1 libffi-dev libfftw3-double3 libfuse2 libgeotiff5 libgit2-1.1 libhttp-parser2.9 libhwloc-plugins
  libhwloc15 libibverbs1 libicu-dev libjs-jquery-ui liblbfgsb0 libllvm11 liblzf1 libmagics++-data libmagplus3v5 libmbedcrypto7 libmbedtls14 libmbedx509-1 libmd4c0 libmysqlclient21 libncurses-dev libodc-0d
  libopenblas-dev libopenblas-pthread-dev libopenblas0 libopenblas0-pthread libopenmpi3 libpcre2-16-0 libpfm4 libpmix2 libpq5 libpsm-infinipath1 libpsm2-2 libqhull-r8.0 libqt5core5a libqt5dbus5 libqt5gui5
  libqt5network5 libqt5svg5 libqt5widgets5 librdmacm1 libssh2-1 libtbb12 libtbbmalloc2 libterralib3 libtinfo-dev libucx0 libxcb-xinerama0 libxcb-xinput0 libxml2-dev libxnvctrl0 libxsimd-dev libz3-4 libz3-dev
  llvm-11 llvm-11-dev llvm-11-linker-tools llvm-11-runtime llvm-11-tools mysql-common numba-doc python-babel-localedata python-matplotlib-data python-odf-doc python-odf-tools python-tables-data python3-appdirs
  python3-asciitree python3-attr python3-babel python3-beniget python3-blosc python3-bottleneck python3-brotli python3-bs4 python3-cdo python3-cftime python3-cloudpickle python3-cycler python3-dask
  python3-decorator python3-defusedxml python3-distributed python3-dropbox python3-et-xmlfile python3-fonttools python3-fs python3-fsspec python3-fusepy python3-gast python3-h5netcdf python3-h5py-serial
  python3-heapdict python3-html5lib python3-iniconfig python3-jdcal python3-jinja2 python3-kiwisolver python3-libarchive-c python3-llvmlite python3-locket python3-lxml python3-lz4 python3-matplotlib
  python3-mpmath python3-msgpack python3-netcdf4 python3-numba python3-numcodecs python3-numexpr python3-numpy python3-odf python3-openpyxl python3-packaging python3-pandas python3-pandas-lib python3-partd
  python3-pil.imagetk python3-pluggy python3-ply python3-psutil python3-py python3-pygit2 python3-pygments python3-pytest python3-pythran python3-scipy python3-sortedcontainers python3-soupsieve python3-stone
  python3-sympy python3-tables python3-tables-lib python3-tblib python3-tk python3-toml python3-toolz python3-tornado python3-ufolib2 python3-unicodedata2 python3-webencodings python3-xarray python3-xlwt
  python3-zarr python3-zict python3-zmq qt5-gtk-platformtheme qttranslations5-l10n sphinx-rtd-theme-common tk8.6-blt2.5 unicode-data
0 upgraded, 174 newly installed, 0 to remove and 16 not upgraded.
Need to get 260 MB of archives.
After this operation, 1,418 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 fonts-lato all 2.0-2.1 [2,696 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libdouble-conversion3 amd64 3.1.7-4 [39.0 kB]                                                                                                      
Get:3 http://in.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpcre2-16-0 amd64 10.39-3ubuntu0.1 [203 kB]                                                                                                  
Get:4 http://in.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 libqt5core5a amd64 5.15.3+dfsg-2ubuntu0.2 [2,006 kB]                                                                                       
Get:5 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libmd4c0 amd64 0.4.8-1 [42.0 kB]                                                                                                                   
Get:6 http://in.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 libqt5dbus5 amd64 5.15.3+dfsg-2ubuntu0.2 [222 kB]                                                                                          
Get:7 http://in.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 libqt5network5 amd64 5.15.3+dfsg-2ubuntu0.2 [731 kB]                                                                                       
Get:8 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libxcb-xinerama0 amd64 1.14-3ubuntu3 [5,414 B]                                                                                                         
Get:9 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libxcb-xinput0 amd64 1.14-3ubuntu3 [34.3 kB]                                                                                                           
Get:10 http://in.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 libqt5gui5 amd64 5.15.3+dfsg-2ubuntu0.2 [3,722 kB]                                                                                        
Get:11 http://in.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 libqt5widgets5 amd64 5.15.3+dfsg-2ubuntu0.2 [2,561 kB]                                                                                    
Get:12 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libqt5svg5 amd64 5.15.3-1 [149 kB]                                                                                                                
Get:13 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 binfmt-support amd64 2.2.1-2 [55.8 kB]                                                                                                                
Get:14 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 tk8.6-blt2.5 amd64 2.5.3+dfsg-4.1build2 [643 kB]                                                                                                      
Get:15 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 blt amd64 2.5.3+dfsg-4.1build2 [4,838 B]                                                                                                              
Get:16 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libeccodes-data all 2.24.2-1 [1,592 kB]                                                                                                           
Get:17 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libeccodes0 amd64 2.24.2-1 [614 kB]                                                                                                               
Get:18 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libcdi0 amd64 2.0.4-1 [411 kB]                                                                                                                    
Get:19 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libfftw3-double3 amd64 3.3.8-2ubuntu8 [770 kB]                                                                                                        
Get:20 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libmagics++-data all 4.10.1-1 [41.8 MB]                                                                                                           
Get:21 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libopenblas0-pthread amd64 0.3.20+ds-1 [6,803 kB]                                                                                                 
Get:22 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libopenblas0 amd64 0.3.20+ds-1 [6,098 B]                                                                                                          
Get:23 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libevent-core-2.1-7 amd64 2.1.12-stable-1build3 [93.9 kB]                                                                                             
Get:24 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libevent-pthreads-2.1-7 amd64 2.1.12-stable-1build3 [7,642 B]                                                                                         
Get:25 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libibverbs1 amd64 39.0-1 [69.3 kB]                                                                                                                    
Get:26 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 ibverbs-providers amd64 39.0-1 [341 kB]                                                                                                               
Get:27 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libpsm-infinipath1 amd64 3.3+20.604758e7-6.1 [170 kB]                                                                                             
Get:28 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libpsm2-2 amd64 11.2.185-1 [182 kB]                                                                                                               
Get:29 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 librdmacm1 amd64 39.0-1 [71.2 kB]                                                                                                                     
Get:30 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libfabric1 amd64 1.11.0-3 [558 kB]                                                                                                                
Get:31 http://in.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 libhwloc15 amd64 2.7.0-2ubuntu1 [159 kB]                                                                                                  
Get:32 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libxnvctrl0 amd64 510.47.03-0ubuntu1 [11.5 kB]                                                                                                        
Get:33 http://in.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 libhwloc-plugins amd64 2.7.0-2ubuntu1 [15.6 kB]                                                                                           
Get:34 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libpmix2 amd64 4.1.2-2ubuntu1 [604 kB]                                                                                                            
Get:35 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libucx0 amd64 1.12.1~rc2-1 [891 kB]                                                                                                               
Get:36 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libopenmpi3 amd64 4.1.2-2ubuntu1 [2,594 kB]                                                                                                       
Get:37 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libeckit0d amd64 1.18.7-1 [1,306 kB]                                                                                                              
Get:38 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libgeotiff5 amd64 1.7.0-2build1 [67.1 kB]                                                                                                         
Get:39 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libodc-0d amd64 1.4.4-1 [426 kB]                                                                                                                  
Get:40 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libdxflib3 amd64 3.26.4-1 [56.2 kB]                                                                                                               
Get:41 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 mysql-common all 5.8+1.0.8 [7,212 B]                                                                                                                  
Get:42 http://in.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libmysqlclient21 amd64 8.0.32-0ubuntu0.22.04.2 [1,299 kB]                                                                                     
Get:43 http://in.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpq5 amd64 14.6-0ubuntu0.22.04.1 [141 kB]                                                                                                   
Get:44 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libterralib3 amd64 4.3.0+dfsg.2-12.1build2 [2,596 kB]                                                                                             
Get:45 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 fonts-dejavu-extra all 2.37-2build1 [2,041 kB]                                                                                                        
Get:46 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libmagplus3v5 amd64 4.10.1-1 [2,619 kB]                                                                                                           
Get:47 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 cdo amd64 2.0.4-1 [2,419 kB]                                                                                                                      
Get:48 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 fonts-font-awesome all 5.0.10+really4.7.0~dfsg-4.1 [516 kB]                                                                                           
Get:49 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 fonts-lyx all 2.3.6-1 [159 kB]                                                                                                                    
Get:50 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 icu-devtools amd64 70.1-2 [197 kB]                                                                                                                    
Get:51 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libblosc1 amd64 1.21.1+ds2-2 [35.8 kB]                                                                                                            
Get:52 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libboost1.74-dev amd64 1.74.0-14ubuntu3 [9,609 kB]                                                                                                    
Get:53 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libboost-dev amd64 1.74.0.3ubuntu7 [3,490 B]                                                                                                          
Get:54 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libllvm11 amd64 1:11.1.0-6 [19.6 MB]                                                                                                              
Get:55 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libclang-cpp11 amd64 1:11.1.0-6 [10.5 MB]                                                                                                         
Get:56 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libfuse2 amd64 2.9.9-5ubuntu3 [90.3 kB]                                                                                                           
Get:57 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libhttp-parser2.9 amd64 2.9.4-4 [21.5 kB]                                                                                                         
Get:58 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libmbedcrypto7 amd64 2.28.0-1build1 [204 kB]                                                                                                      
Get:59 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libmbedx509-1 amd64 2.28.0-1build1 [47.2 kB]                                                                                                      
Get:60 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libmbedtls14 amd64 2.28.0-1build1 [82.7 kB]                                                                                                       
Get:61 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libssh2-1 amd64 1.10.0-3 [109 kB]                                                                                                                 
Get:62 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libgit2-1.1 amd64 1.1.0+dfsg.1-4.1build1 [456 kB]                                                                                                 
Get:63 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libicu-dev amd64 70.1-2 [11.6 MB]                                                                                                                     
Get:64 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-jquery-ui all 1.13.1+dfsg-1 [253 kB]                                                                                                        
Get:65 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 liblbfgsb0 amd64 3.0+dfsg.3-10 [29.9 kB]                                                                                                          
Get:66 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 liblzf1 amd64 3.6-3 [7,444 B]                                                                                                                     
Get:67 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libncurses-dev amd64 6.3-2 [380 kB]                                                                                                                   
Get:68 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libopenblas-pthread-dev amd64 0.3.20+ds-1 [4,634 kB]                                                                                              
Get:69 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libopenblas-dev amd64 0.3.20+ds-1 [18.6 kB]                                                                                                       
Get:70 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libqhull-r8.0 amd64 2020.2-4 [196 kB]                                                                                                             
Get:71 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libtbbmalloc2 amd64 2021.5.0-7ubuntu2 [49.6 kB]                                                                                                   
Get:72 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libtbb12 amd64 2021.5.0-7ubuntu2 [84.8 kB]                                                                                                        
Get:73 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libtinfo-dev amd64 6.3-2 [774 B]                                                                                                                      
Get:74 http://in.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libxml2-dev amd64 2.9.13+dfsg-1ubuntu0.2 [804 kB]                                                                                             
Get:75 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libxsimd-dev amd64 7.6.0-2 [108 kB]                                                                                                               
Get:76 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 llvm-11-runtime amd64 1:11.1.0-6 [186 kB]                                                                                                         
Get:77 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 llvm-11-linker-tools amd64 1:11.1.0-6 [1,275 kB]                                                                                                  
Get:78 http://in.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpfm4 amd64 4.11.1+git32-gd0b85fb-1ubuntu0.1 [345 kB]                                                                                       
Get:79 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 llvm-11 amd64 1:11.1.0-6 [9,118 kB]                                                                                                               
Get:80 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 libffi-dev amd64 3.4.2-4 [63.7 kB]                                                                                                                    
Get:81 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-pygments all 2.11.2+dfsg-2 [750 kB]                                                                                                           
Get:82 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 llvm-11-tools amd64 1:11.1.0-6 [359 kB]                                                                                                           
Get:83 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libz3-4 amd64 4.8.12-1 [5,766 kB]                                                                                                                 
Get:84 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 libz3-dev amd64 4.8.12-1 [72.2 kB]                                                                                                                
Get:85 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 llvm-11-dev amd64 1:11.1.0-6 [29.9 MB]                                                                                                            
Get:86 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 sphinx-rtd-theme-common all 1.0.0+dfsg-1 [991 kB]                                                                                                     
Get:87 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 numba-doc all 0.55.1-0ubuntu2 [737 kB]                                                                                                            
Get:88 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python-babel-localedata all 2.8.0+dfsg.1-7 [4,982 kB]                                                                                                 
Get:89 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python-matplotlib-data all 3.5.1-2build1 [2,942 kB]                                                                                               
Get:90 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python-odf-doc all 1.4.2-1 [222 kB]                                                                                                               
Get:91 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-defusedxml all 0.7.1-1 [43.2 kB]                                                                                                              
Get:92 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-odf all 1.4.2-1 [79.3 kB]                                                                                                                 
Get:93 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python-odf-tools all 1.4.2-1 [27.3 kB]                                                                                                            
Get:94 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python-tables-data all 3.7.0-2build1 [47.6 kB]                                                                                                    
Get:95 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-appdirs all 1.4.4-2 [11.4 kB]                                                                                                                 
Get:96 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-asciitree all 0.3.3-3 [5,432 B]                                                                                                           
Get:97 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-attr all 21.2.0-1 [44.0 kB]                                                                                                                   
Get:98 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-babel all 2.8.0+dfsg.1-7 [85.1 kB]                                                                                                            
Get:99 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-gast all 0.5.2-2 [9,394 B]                                                                                                                
Get:100 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-beniget all 0.4.1-2 [9,904 B]                                                                                                            
Get:101 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-blosc amd64 1.9.2+ds1-3build2 [29.3 kB]                                                                                                  
Get:102 http://in.archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3-numpy amd64 1:1.21.5-1ubuntu22.04.1 [3,467 kB]                                                                                       
Get:103 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-bottleneck amd64 1.3.2+ds1-2build1 [82.9 kB]                                                                                             
Get:104 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-brotli amd64 1.0.9-2build6 [319 kB]                                                                                                      
Get:105 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-soupsieve all 2.3.1-1 [33.0 kB]                                                                                                              
Get:106 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-bs4 all 4.10.0-2 [79.1 kB]                                                                                                                   
Get:107 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-cftime amd64 1.5.2+ds-1build1 [174 kB]                                                                                                   
Get:108 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-cloudpickle all 2.0.0-1 [24.5 kB]                                                                                                        
Get:109 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-cycler all 0.11.0-1 [8,156 B]                                                                                                            
Get:110 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-fsspec all 2022.01.0-1 [96.8 kB]                                                                                                         
Get:111 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-toolz all 0.11.2-1 [44.7 kB]                                                                                                             
Get:112 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-packaging all 21.3-1 [30.7 kB]                                                                                                               
Get:113 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-locket all 0.2.1-1 [5,390 B]                                                                                                             
Get:114 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-partd all 1.2.0-1 [15.8 kB]                                                                                                              
Get:115 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-dask all 2022.01.0+dfsg-1ubuntu1 [724 kB]                                                                                                
Get:116 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-decorator all 4.4.2-0ubuntu1 [10.3 kB]                                                                                                       
Get:117 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-jinja2 all 3.0.3-1 [108 kB]                                                                                                                  
Get:118 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-msgpack amd64 1.0.3-1build1 [67.8 kB]                                                                                                        
Get:119 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-psutil amd64 5.9.0-1build1 [158 kB]                                                                                                          
Get:120 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-sortedcontainers all 2.1.0-2 [27.3 kB]                                                                                                       
Get:121 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-tblib all 1.7.0-2 [12.7 kB]                                                                                                              
Get:122 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-tornado amd64 6.1.0-3build1 [287 kB]                                                                                                     
Get:123 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-heapdict all 1.0.1-1 [5,324 B]                                                                                                           
Get:124 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-zict all 2.0.0-1 [9,440 B]                                                                                                               
Get:125 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-distributed all 2022.01.0+ds.1-1 [575 kB]                                                                                                
Get:126 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-ply all 3.11-5 [47.5 kB]                                                                                                                     
Get:127 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-stone all 3.3.1-1 [119 kB]                                                                                                               
Get:128 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-dropbox all 11.26.0-1 [405 kB]                                                                                                           
Get:129 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-et-xmlfile all 1.0.1-2.1 [9,224 B]                                                                                                       
Get:130 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-pythran amd64 0.10.0+ds2-1 [423 kB]                                                                                                      
Get:131 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-scipy amd64 1.8.0-1exp2ubuntu1 [14.7 MB]                                                                                                 
Get:132 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-ufolib2 all 0.13.1+dfsg1-1 [32.2 kB]                                                                                                     
Get:133 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-mpmath all 1.2.1-2 [419 kB]                                                                                                              
Get:134 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-sympy all 1.9-1 [4,312 kB]                                                                                                               
Get:135 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-fs all 2.4.12-1 [84.9 kB]                                                                                                                
Get:136 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-lxml amd64 4.8.0-1build1 [1,150 kB]                                                                                                          
Get:137 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-lz4 amd64 3.1.3+dfsg-1build3 [33.3 kB]                                                                                                   
Get:138 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-unicodedata2 amd64 14.0.0+ds-8 [376 kB]                                                                                                  
Get:139 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 unicode-data all 14.0.0-1.1 [8,206 kB]                                                                                                           
Get:140 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-fonttools amd64 4.29.1-2build1 [810 kB]                                                                                                  
Get:141 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-fusepy all 3.0.1-2 [11.3 kB]                                                                                                             
Get:142 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-h5py-serial amd64 3.6.0-2build1 [872 kB]                                                                                                 
Get:143 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-h5netcdf all 0.12.0-1 [19.3 kB]                                                                                                          
Get:144 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-webencodings all 0.5.1-4 [11.8 kB]                                                                                                           
Get:145 http://in.archive.ubuntu.com/ubuntu jammy/main amd64 python3-html5lib all 1.1-3 [87.0 kB]                                                                                                                 
Get:146 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-iniconfig all 1.1.1-2 [6,024 B]                                                                                                          
Get:147 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-jdcal all 1.0-1.3 [7,944 B]                                                                                                              
Get:148 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-kiwisolver amd64 1.3.2-1build1 [48.0 kB]                                                                                                 
Get:149 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-llvmlite amd64 0.38.0-1 [126 kB]                                                                                                         
Get:150 http://in.archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3-tk amd64 3.10.6-1~22.04 [110 kB]                                                                                                     
Get:151 http://in.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 python3-pil.imagetk amd64 9.0.1-1ubuntu0.1 [9,608 B]                                                                                     
Get:152 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-matplotlib amd64 3.5.1-2build1 [5,937 kB]                                                                                                
Get:153 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-netcdf4 amd64 1.5.8-1build1 [449 kB]                                                                                                     
Get:154 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-numba amd64 0.55.1-0ubuntu2 [1,588 kB]                                                                                                   
Get:155 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-numcodecs amd64 0.9.1+ds-2build1 [268 kB]                                                                                                
Get:156 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-numexpr amd64 2.8.1-1build1 [86.0 kB]                                                                                                    
Get:157 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-openpyxl all 3.0.9-1 [148 kB]                                                                                                            
Get:158 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-pandas-lib amd64 1.3.5+dfsg-3 [3,735 kB]                                                                                                 
Get:159 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-pandas all 1.3.5+dfsg-3 [2,680 kB]                                                                                                       
Get:160 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-pluggy all 0.13.0-7.1 [19.0 kB]                                                                                                          
Get:161 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-py all 1.10.0-1 [71.9 kB]                                                                                                                
Get:162 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-pygit2 amd64 1.6.1+dfsg-2 [154 kB]                                                                                                       
Get:163 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-toml all 0.10.2-1 [16.5 kB]                                                                                                              
Get:164 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-pytest all 6.2.5-1ubuntu2 [214 kB]                                                                                                       
Get:165 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-tables-lib amd64 3.7.0-2build1 [427 kB]                                                                                                  
Get:166 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-tables all 3.7.0-2build1 [333 kB]                                                                                                        
Get:167 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-xarray all 0.21.1-1 [575 kB]                                                                                                             
Get:168 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-xlwt all 1.3.0-3 [83.7 kB]                                                                                                               
Get:169 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-zarr all 2.10.3+ds-1 [260 kB]                                                                                                            
Get:170 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-zmq amd64 22.3.0-1build1 [283 kB]                                                                                                        
Get:171 http://in.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 qt5-gtk-platformtheme amd64 5.15.3+dfsg-2ubuntu0.2 [130 kB]                                                                              
Get:172 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 qttranslations5-l10n all 5.15.3-1 [1,983 kB]                                                                                                     
Get:173 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-cdo amd64 1.5.6-1 [12.1 kB]                                                                                                              
Get:174 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-libarchive-c all 2.9-0.1 [14.5 kB]                                                                                                       
Fetched 260 MB in 4min 8s (1,047 kB/s)                                                                                                                                                                            
Extracting templates from packages: 100%
Selecting previously unselected package fonts-lato.
(Reading database ... 214129 files and directories currently installed.)
Preparing to unpack .../000-fonts-lato_2.0-2.1_all.deb ...
Unpacking fonts-lato (2.0-2.1) ...
Selecting previously unselected package libdouble-conversion3:amd64.
Preparing to unpack .../001-libdouble-conversion3_3.1.7-4_amd64.deb ...
Unpacking libdouble-conversion3:amd64 (3.1.7-4) ...
Selecting previously unselected package libpcre2-16-0:amd64.
Preparing to unpack .../002-libpcre2-16-0_10.39-3ubuntu0.1_amd64.deb ...
Unpacking libpcre2-16-0:amd64 (10.39-3ubuntu0.1) ...
Selecting previously unselected package libqt5core5a:amd64.
Preparing to unpack .../003-libqt5core5a_5.15.3+dfsg-2ubuntu0.2_amd64.deb ...
Unpacking libqt5core5a:amd64 (5.15.3+dfsg-2ubuntu0.2) ...
Selecting previously unselected package libmd4c0:amd64.
Preparing to unpack .../004-libmd4c0_0.4.8-1_amd64.deb ...
Unpacking libmd4c0:amd64 (0.4.8-1) ...
Selecting previously unselected package libqt5dbus5:amd64.
Preparing to unpack .../005-libqt5dbus5_5.15.3+dfsg-2ubuntu0.2_amd64.deb ...
Unpacking libqt5dbus5:amd64 (5.15.3+dfsg-2ubuntu0.2) ...
Selecting previously unselected package libqt5network5:amd64.
Preparing to unpack .../006-libqt5network5_5.15.3+dfsg-2ubuntu0.2_amd64.deb ...
Unpacking libqt5network5:amd64 (5.15.3+dfsg-2ubuntu0.2) ...
Selecting previously unselected package libxcb-xinerama0:amd64.
Preparing to unpack .../007-libxcb-xinerama0_1.14-3ubuntu3_amd64.deb ...
Unpacking libxcb-xinerama0:amd64 (1.14-3ubuntu3) ...
Selecting previously unselected package libxcb-xinput0:amd64.
Preparing to unpack .../008-libxcb-xinput0_1.14-3ubuntu3_amd64.deb ...
Unpacking libxcb-xinput0:amd64 (1.14-3ubuntu3) ...
Selecting previously unselected package libqt5gui5:amd64.
Preparing to unpack .../009-libqt5gui5_5.15.3+dfsg-2ubuntu0.2_amd64.deb ...
Unpacking libqt5gui5:amd64 (5.15.3+dfsg-2ubuntu0.2) ...
Selecting previously unselected package libqt5widgets5:amd64.
Preparing to unpack .../010-libqt5widgets5_5.15.3+dfsg-2ubuntu0.2_amd64.deb ...
Unpacking libqt5widgets5:amd64 (5.15.3+dfsg-2ubuntu0.2) ...
Selecting previously unselected package libqt5svg5:amd64.
Preparing to unpack .../011-libqt5svg5_5.15.3-1_amd64.deb ...
Unpacking libqt5svg5:amd64 (5.15.3-1) ...
Selecting previously unselected package binfmt-support.
Preparing to unpack .../012-binfmt-support_2.2.1-2_amd64.deb ...
Unpacking binfmt-support (2.2.1-2) ...
Selecting previously unselected package tk8.6-blt2.5.
Preparing to unpack .../013-tk8.6-blt2.5_2.5.3+dfsg-4.1build2_amd64.deb ...
Unpacking tk8.6-blt2.5 (2.5.3+dfsg-4.1build2) ...
Selecting previously unselected package blt.
Preparing to unpack .../014-blt_2.5.3+dfsg-4.1build2_amd64.deb ...
Unpacking blt (2.5.3+dfsg-4.1build2) ...
Selecting previously unselected package libeccodes-data.
Preparing to unpack .../015-libeccodes-data_2.24.2-1_all.deb ...
Unpacking libeccodes-data (2.24.2-1) ...
Selecting previously unselected package libeccodes0:amd64.
Preparing to unpack .../016-libeccodes0_2.24.2-1_amd64.deb ...
Unpacking libeccodes0:amd64 (2.24.2-1) ...
Selecting previously unselected package libcdi0:amd64.
Preparing to unpack .../017-libcdi0_2.0.4-1_amd64.deb ...
Unpacking libcdi0:amd64 (2.0.4-1) ...
Selecting previously unselected package libfftw3-double3:amd64.
Preparing to unpack .../018-libfftw3-double3_3.3.8-2ubuntu8_amd64.deb ...
Unpacking libfftw3-double3:amd64 (3.3.8-2ubuntu8) ...
Selecting previously unselected package libmagics++-data.
Preparing to unpack .../019-libmagics++-data_4.10.1-1_all.deb ...
Unpacking libmagics++-data (4.10.1-1) ...
Selecting previously unselected package libopenblas0-pthread:amd64.
Preparing to unpack .../020-libopenblas0-pthread_0.3.20+ds-1_amd64.deb ...
Unpacking libopenblas0-pthread:amd64 (0.3.20+ds-1) ...
Selecting previously unselected package libopenblas0:amd64.
Preparing to unpack .../021-libopenblas0_0.3.20+ds-1_amd64.deb ...
Unpacking libopenblas0:amd64 (0.3.20+ds-1) ...
Selecting previously unselected package libevent-core-2.1-7:amd64.
Preparing to unpack .../022-libevent-core-2.1-7_2.1.12-stable-1build3_amd64.deb ...
Unpacking libevent-core-2.1-7:amd64 (2.1.12-stable-1build3) ...
Selecting previously unselected package libevent-pthreads-2.1-7:amd64.
Preparing to unpack .../023-libevent-pthreads-2.1-7_2.1.12-stable-1build3_amd64.deb ...
Unpacking libevent-pthreads-2.1-7:amd64 (2.1.12-stable-1build3) ...
Selecting previously unselected package libibverbs1:amd64.
Preparing to unpack .../024-libibverbs1_39.0-1_amd64.deb ...
Unpacking libibverbs1:amd64 (39.0-1) ...
Selecting previously unselected package ibverbs-providers:amd64.
Preparing to unpack .../025-ibverbs-providers_39.0-1_amd64.deb ...
Unpacking ibverbs-providers:amd64 (39.0-1) ...
Selecting previously unselected package libpsm-infinipath1.
Preparing to unpack .../026-libpsm-infinipath1_3.3+20.604758e7-6.1_amd64.deb ...
Unpacking libpsm-infinipath1 (3.3+20.604758e7-6.1) ...
Selecting previously unselected package libpsm2-2.
Preparing to unpack .../027-libpsm2-2_11.2.185-1_amd64.deb ...
Unpacking libpsm2-2 (11.2.185-1) ...
Selecting previously unselected package librdmacm1:amd64.
Preparing to unpack .../028-librdmacm1_39.0-1_amd64.deb ...
Unpacking librdmacm1:amd64 (39.0-1) ...
Selecting previously unselected package libfabric1:amd64.
Preparing to unpack .../029-libfabric1_1.11.0-3_amd64.deb ...
Unpacking libfabric1:amd64 (1.11.0-3) ...
Selecting previously unselected package libhwloc15:amd64.
Preparing to unpack .../030-libhwloc15_2.7.0-2ubuntu1_amd64.deb ...
Unpacking libhwloc15:amd64 (2.7.0-2ubuntu1) ...
Selecting previously unselected package libxnvctrl0:amd64.
Preparing to unpack .../031-libxnvctrl0_510.47.03-0ubuntu1_amd64.deb ...
Unpacking libxnvctrl0:amd64 (510.47.03-0ubuntu1) ...
Selecting previously unselected package libhwloc-plugins:amd64.
Preparing to unpack .../032-libhwloc-plugins_2.7.0-2ubuntu1_amd64.deb ...
Unpacking libhwloc-plugins:amd64 (2.7.0-2ubuntu1) ...
Selecting previously unselected package libpmix2:amd64.
Preparing to unpack .../033-libpmix2_4.1.2-2ubuntu1_amd64.deb ...
Unpacking libpmix2:amd64 (4.1.2-2ubuntu1) ...
Selecting previously unselected package libucx0:amd64.
Preparing to unpack .../034-libucx0_1.12.1~rc2-1_amd64.deb ...
Unpacking libucx0:amd64 (1.12.1~rc2-1) ...
Selecting previously unselected package libopenmpi3:amd64.
Preparing to unpack .../035-libopenmpi3_4.1.2-2ubuntu1_amd64.deb ...
Unpacking libopenmpi3:amd64 (4.1.2-2ubuntu1) ...
Selecting previously unselected package libeckit0d:amd64.
Preparing to unpack .../036-libeckit0d_1.18.7-1_amd64.deb ...
Unpacking libeckit0d:amd64 (1.18.7-1) ...
Selecting previously unselected package libgeotiff5:amd64.
Preparing to unpack .../037-libgeotiff5_1.7.0-2build1_amd64.deb ...
Unpacking libgeotiff5:amd64 (1.7.0-2build1) ...
Selecting previously unselected package libodc-0d:amd64.
Preparing to unpack .../038-libodc-0d_1.4.4-1_amd64.deb ...
Unpacking libodc-0d:amd64 (1.4.4-1) ...
Selecting previously unselected package libdxflib3:amd64.
Preparing to unpack .../039-libdxflib3_3.26.4-1_amd64.deb ...
Unpacking libdxflib3:amd64 (3.26.4-1) ...
Selecting previously unselected package mysql-common.
Preparing to unpack .../040-mysql-common_5.8+1.0.8_all.deb ...
Unpacking mysql-common (5.8+1.0.8) ...
Selecting previously unselected package libmysqlclient21:amd64.
Preparing to unpack .../041-libmysqlclient21_8.0.32-0ubuntu0.22.04.2_amd64.deb ...
Unpacking libmysqlclient21:amd64 (8.0.32-0ubuntu0.22.04.2) ...
Selecting previously unselected package libpq5:amd64.
Preparing to unpack .../042-libpq5_14.6-0ubuntu0.22.04.1_amd64.deb ...
Unpacking libpq5:amd64 (14.6-0ubuntu0.22.04.1) ...
Selecting previously unselected package libterralib3:amd64.
Preparing to unpack .../043-libterralib3_4.3.0+dfsg.2-12.1build2_amd64.deb ...
Unpacking libterralib3:amd64 (4.3.0+dfsg.2-12.1build2) ...
Selecting previously unselected package fonts-dejavu-extra.
Preparing to unpack .../044-fonts-dejavu-extra_2.37-2build1_all.deb ...
Unpacking fonts-dejavu-extra (2.37-2build1) ...
Selecting previously unselected package libmagplus3v5:amd64.
Preparing to unpack .../045-libmagplus3v5_4.10.1-1_amd64.deb ...
Unpacking libmagplus3v5:amd64 (4.10.1-1) ...
Selecting previously unselected package cdo.
Preparing to unpack .../046-cdo_2.0.4-1_amd64.deb ...
Unpacking cdo (2.0.4-1) ...
Selecting previously unselected package fonts-font-awesome.
Preparing to unpack .../047-fonts-font-awesome_5.0.10+really4.7.0~dfsg-4.1_all.deb ...
Unpacking fonts-font-awesome (5.0.10+really4.7.0~dfsg-4.1) ...
Selecting previously unselected package fonts-lyx.
Preparing to unpack .../048-fonts-lyx_2.3.6-1_all.deb ...
Unpacking fonts-lyx (2.3.6-1) ...
Selecting previously unselected package icu-devtools.
Preparing to unpack .../049-icu-devtools_70.1-2_amd64.deb ...
Unpacking icu-devtools (70.1-2) ...
Selecting previously unselected package libblosc1:amd64.
Preparing to unpack .../050-libblosc1_1.21.1+ds2-2_amd64.deb ...
Unpacking libblosc1:amd64 (1.21.1+ds2-2) ...
Selecting previously unselected package libboost1.74-dev:amd64.
Preparing to unpack .../051-libboost1.74-dev_1.74.0-14ubuntu3_amd64.deb ...
Unpacking libboost1.74-dev:amd64 (1.74.0-14ubuntu3) ...
Selecting previously unselected package libboost-dev:amd64.
Preparing to unpack .../052-libboost-dev_1.74.0.3ubuntu7_amd64.deb ...
Unpacking libboost-dev:amd64 (1.74.0.3ubuntu7) ...
Selecting previously unselected package libllvm11:amd64.
Preparing to unpack .../053-libllvm11_1%3a11.1.0-6_amd64.deb ...
Unpacking libllvm11:amd64 (1:11.1.0-6) ...
Selecting previously unselected package libclang-cpp11.
Preparing to unpack .../054-libclang-cpp11_1%3a11.1.0-6_amd64.deb ...
Unpacking libclang-cpp11 (1:11.1.0-6) ...
Selecting previously unselected package libfuse2:amd64.
Preparing to unpack .../055-libfuse2_2.9.9-5ubuntu3_amd64.deb ...
Unpacking libfuse2:amd64 (2.9.9-5ubuntu3) ...
Selecting previously unselected package libhttp-parser2.9:amd64.
Preparing to unpack .../056-libhttp-parser2.9_2.9.4-4_amd64.deb ...
Unpacking libhttp-parser2.9:amd64 (2.9.4-4) ...
Selecting previously unselected package libmbedcrypto7:amd64.
Preparing to unpack .../057-libmbedcrypto7_2.28.0-1build1_amd64.deb ...
Unpacking libmbedcrypto7:amd64 (2.28.0-1build1) ...
Selecting previously unselected package libmbedx509-1:amd64.
Preparing to unpack .../058-libmbedx509-1_2.28.0-1build1_amd64.deb ...
Unpacking libmbedx509-1:amd64 (2.28.0-1build1) ...
Selecting previously unselected package libmbedtls14:amd64.
Preparing to unpack .../059-libmbedtls14_2.28.0-1build1_amd64.deb ...
Unpacking libmbedtls14:amd64 (2.28.0-1build1) ...
Selecting previously unselected package libssh2-1:amd64.
Preparing to unpack .../060-libssh2-1_1.10.0-3_amd64.deb ...
Unpacking libssh2-1:amd64 (1.10.0-3) ...
Selecting previously unselected package libgit2-1.1:amd64.
Preparing to unpack .../061-libgit2-1.1_1.1.0+dfsg.1-4.1build1_amd64.deb ...
Unpacking libgit2-1.1:amd64 (1.1.0+dfsg.1-4.1build1) ...
Selecting previously unselected package libicu-dev:amd64.
Preparing to unpack .../062-libicu-dev_70.1-2_amd64.deb ...
Unpacking libicu-dev:amd64 (70.1-2) ...
Selecting previously unselected package libjs-jquery-ui.
Preparing to unpack .../063-libjs-jquery-ui_1.13.1+dfsg-1_all.deb ...
Unpacking libjs-jquery-ui (1.13.1+dfsg-1) ...
Selecting previously unselected package liblbfgsb0:amd64.
Preparing to unpack .../064-liblbfgsb0_3.0+dfsg.3-10_amd64.deb ...
Unpacking liblbfgsb0:amd64 (3.0+dfsg.3-10) ...
Selecting previously unselected package liblzf1:amd64.
Preparing to unpack .../065-liblzf1_3.6-3_amd64.deb ...
Unpacking liblzf1:amd64 (3.6-3) ...
Selecting previously unselected package libncurses-dev:amd64.
Preparing to unpack .../066-libncurses-dev_6.3-2_amd64.deb ...
Unpacking libncurses-dev:amd64 (6.3-2) ...
Selecting previously unselected package libopenblas-pthread-dev:amd64.
Preparing to unpack .../067-libopenblas-pthread-dev_0.3.20+ds-1_amd64.deb ...
Unpacking libopenblas-pthread-dev:amd64 (0.3.20+ds-1) ...
Selecting previously unselected package libopenblas-dev:amd64.
Preparing to unpack .../068-libopenblas-dev_0.3.20+ds-1_amd64.deb ...
Unpacking libopenblas-dev:amd64 (0.3.20+ds-1) ...
Selecting previously unselected package libqhull-r8.0:amd64.
Preparing to unpack .../069-libqhull-r8.0_2020.2-4_amd64.deb ...
Unpacking libqhull-r8.0:amd64 (2020.2-4) ...
Selecting previously unselected package libtbbmalloc2:amd64.
Preparing to unpack .../070-libtbbmalloc2_2021.5.0-7ubuntu2_amd64.deb ...
Unpacking libtbbmalloc2:amd64 (2021.5.0-7ubuntu2) ...
Selecting previously unselected package libtbb12:amd64.
Preparing to unpack .../071-libtbb12_2021.5.0-7ubuntu2_amd64.deb ...
Unpacking libtbb12:amd64 (2021.5.0-7ubuntu2) ...
Selecting previously unselected package libtinfo-dev:amd64.
Preparing to unpack .../072-libtinfo-dev_6.3-2_amd64.deb ...
Unpacking libtinfo-dev:amd64 (6.3-2) ...
Selecting previously unselected package libxml2-dev:amd64.
Preparing to unpack .../073-libxml2-dev_2.9.13+dfsg-1ubuntu0.2_amd64.deb ...
Unpacking libxml2-dev:amd64 (2.9.13+dfsg-1ubuntu0.2) ...
Selecting previously unselected package libxsimd-dev:amd64.
Preparing to unpack .../074-libxsimd-dev_7.6.0-2_amd64.deb ...
Unpacking libxsimd-dev:amd64 (7.6.0-2) ...
Selecting previously unselected package llvm-11-runtime.
Preparing to unpack .../075-llvm-11-runtime_1%3a11.1.0-6_amd64.deb ...
Unpacking llvm-11-runtime (1:11.1.0-6) ...
Selecting previously unselected package llvm-11-linker-tools.
Preparing to unpack .../076-llvm-11-linker-tools_1%3a11.1.0-6_amd64.deb ...
Unpacking llvm-11-linker-tools (1:11.1.0-6) ...
Selecting previously unselected package libpfm4:amd64.
Preparing to unpack .../077-libpfm4_4.11.1+git32-gd0b85fb-1ubuntu0.1_amd64.deb ...
Unpacking libpfm4:amd64 (4.11.1+git32-gd0b85fb-1ubuntu0.1) ...
Selecting previously unselected package llvm-11.
Preparing to unpack .../078-llvm-11_1%3a11.1.0-6_amd64.deb ...
Unpacking llvm-11 (1:11.1.0-6) ...
Selecting previously unselected package libffi-dev:amd64.
Preparing to unpack .../079-libffi-dev_3.4.2-4_amd64.deb ...
Unpacking libffi-dev:amd64 (3.4.2-4) ...
Selecting previously unselected package python3-pygments.
Preparing to unpack .../080-python3-pygments_2.11.2+dfsg-2_all.deb ...
Unpacking python3-pygments (2.11.2+dfsg-2) ...
Selecting previously unselected package llvm-11-tools.
Preparing to unpack .../081-llvm-11-tools_1%3a11.1.0-6_amd64.deb ...
Unpacking llvm-11-tools (1:11.1.0-6) ...
Selecting previously unselected package libz3-4:amd64.
Preparing to unpack .../082-libz3-4_4.8.12-1_amd64.deb ...
Unpacking libz3-4:amd64 (4.8.12-1) ...
Selecting previously unselected package libz3-dev:amd64.
Preparing to unpack .../083-libz3-dev_4.8.12-1_amd64.deb ...
Unpacking libz3-dev:amd64 (4.8.12-1) ...
Selecting previously unselected package llvm-11-dev.
Preparing to unpack .../084-llvm-11-dev_1%3a11.1.0-6_amd64.deb ...
Unpacking llvm-11-dev (1:11.1.0-6) ...
Selecting previously unselected package sphinx-rtd-theme-common.
Preparing to unpack .../085-sphinx-rtd-theme-common_1.0.0+dfsg-1_all.deb ...
Unpacking sphinx-rtd-theme-common (1.0.0+dfsg-1) ...
Selecting previously unselected package numba-doc.
Preparing to unpack .../086-numba-doc_0.55.1-0ubuntu2_all.deb ...
Unpacking numba-doc (0.55.1-0ubuntu2) ...
Selecting previously unselected package python-babel-localedata.
Preparing to unpack .../087-python-babel-localedata_2.8.0+dfsg.1-7_all.deb ...
Unpacking python-babel-localedata (2.8.0+dfsg.1-7) ...
Selecting previously unselected package python-matplotlib-data.
Preparing to unpack .../088-python-matplotlib-data_3.5.1-2build1_all.deb ...
Unpacking python-matplotlib-data (3.5.1-2build1) ...
Selecting previously unselected package python-odf-doc.
Preparing to unpack .../089-python-odf-doc_1.4.2-1_all.deb ...
Unpacking python-odf-doc (1.4.2-1) ...
Selecting previously unselected package python3-defusedxml.
Preparing to unpack .../090-python3-defusedxml_0.7.1-1_all.deb ...
Unpacking python3-defusedxml (0.7.1-1) ...
Selecting previously unselected package python3-odf.
Preparing to unpack .../091-python3-odf_1.4.2-1_all.deb ...
Unpacking python3-odf (1.4.2-1) ...
Selecting previously unselected package python-odf-tools.
Preparing to unpack .../092-python-odf-tools_1.4.2-1_all.deb ...
Unpacking python-odf-tools (1.4.2-1) ...
Selecting previously unselected package python-tables-data.
Preparing to unpack .../093-python-tables-data_3.7.0-2build1_all.deb ...
Unpacking python-tables-data (3.7.0-2build1) ...
Selecting previously unselected package python3-appdirs.
Preparing to unpack .../094-python3-appdirs_1.4.4-2_all.deb ...
Unpacking python3-appdirs (1.4.4-2) ...
Selecting previously unselected package python3-asciitree.
Preparing to unpack .../095-python3-asciitree_0.3.3-3_all.deb ...
Unpacking python3-asciitree (0.3.3-3) ...
Selecting previously unselected package python3-attr.
Preparing to unpack .../096-python3-attr_21.2.0-1_all.deb ...
Unpacking python3-attr (21.2.0-1) ...
Selecting previously unselected package python3-babel.
Preparing to unpack .../097-python3-babel_2.8.0+dfsg.1-7_all.deb ...
Unpacking python3-babel (2.8.0+dfsg.1-7) ...
Selecting previously unselected package python3-gast.
Preparing to unpack .../098-python3-gast_0.5.2-2_all.deb ...
Unpacking python3-gast (0.5.2-2) ...
Selecting previously unselected package python3-beniget.
Preparing to unpack .../099-python3-beniget_0.4.1-2_all.deb ...
Unpacking python3-beniget (0.4.1-2) ...
Selecting previously unselected package python3-blosc.
Preparing to unpack .../100-python3-blosc_1.9.2+ds1-3build2_amd64.deb ...
Unpacking python3-blosc (1.9.2+ds1-3build2) ...
Selecting previously unselected package python3-numpy.
Preparing to unpack .../101-python3-numpy_1%3a1.21.5-1ubuntu22.04.1_amd64.deb ...
Unpacking python3-numpy (1:1.21.5-1ubuntu22.04.1) ...
Selecting previously unselected package python3-bottleneck.
Preparing to unpack .../102-python3-bottleneck_1.3.2+ds1-2build1_amd64.deb ...
Unpacking python3-bottleneck (1.3.2+ds1-2build1) ...
Selecting previously unselected package python3-brotli.
Preparing to unpack .../103-python3-brotli_1.0.9-2build6_amd64.deb ...
Unpacking python3-brotli (1.0.9-2build6) ...
Selecting previously unselected package python3-soupsieve.
Preparing to unpack .../104-python3-soupsieve_2.3.1-1_all.deb ...
Unpacking python3-soupsieve (2.3.1-1) ...
Selecting previously unselected package python3-bs4.
Preparing to unpack .../105-python3-bs4_4.10.0-2_all.deb ...
Unpacking python3-bs4 (4.10.0-2) ...
Selecting previously unselected package python3-cftime.
Preparing to unpack .../106-python3-cftime_1.5.2+ds-1build1_amd64.deb ...
Unpacking python3-cftime (1.5.2+ds-1build1) ...
Selecting previously unselected package python3-cloudpickle.
Preparing to unpack .../107-python3-cloudpickle_2.0.0-1_all.deb ...
Unpacking python3-cloudpickle (2.0.0-1) ...
Selecting previously unselected package python3-cycler.
Preparing to unpack .../108-python3-cycler_0.11.0-1_all.deb ...
Unpacking python3-cycler (0.11.0-1) ...
Selecting previously unselected package python3-fsspec.
Preparing to unpack .../109-python3-fsspec_2022.01.0-1_all.deb ...
Unpacking python3-fsspec (2022.01.0-1) ...
Selecting previously unselected package python3-toolz.
Preparing to unpack .../110-python3-toolz_0.11.2-1_all.deb ...
Unpacking python3-toolz (0.11.2-1) ...
Selecting previously unselected package python3-packaging.
Preparing to unpack .../111-python3-packaging_21.3-1_all.deb ...
Unpacking python3-packaging (21.3-1) ...
Selecting previously unselected package python3-locket.
Preparing to unpack .../112-python3-locket_0.2.1-1_all.deb ...
Unpacking python3-locket (0.2.1-1) ...
Selecting previously unselected package python3-partd.
Preparing to unpack .../113-python3-partd_1.2.0-1_all.deb ...
Unpacking python3-partd (1.2.0-1) ...
Selecting previously unselected package python3-dask.
Preparing to unpack .../114-python3-dask_2022.01.0+dfsg-1ubuntu1_all.deb ...
Unpacking python3-dask (2022.01.0+dfsg-1ubuntu1) ...
Selecting previously unselected package python3-decorator.
Preparing to unpack .../115-python3-decorator_4.4.2-0ubuntu1_all.deb ...
Unpacking python3-decorator (4.4.2-0ubuntu1) ...
Selecting previously unselected package python3-jinja2.
Preparing to unpack .../116-python3-jinja2_3.0.3-1_all.deb ...
Unpacking python3-jinja2 (3.0.3-1) ...
Selecting previously unselected package python3-msgpack.
Preparing to unpack .../117-python3-msgpack_1.0.3-1build1_amd64.deb ...
Unpacking python3-msgpack (1.0.3-1build1) ...
Selecting previously unselected package python3-psutil.
Preparing to unpack .../118-python3-psutil_5.9.0-1build1_amd64.deb ...
Unpacking python3-psutil (5.9.0-1build1) ...
Selecting previously unselected package python3-sortedcontainers.
Preparing to unpack .../119-python3-sortedcontainers_2.1.0-2_all.deb ...
Unpacking python3-sortedcontainers (2.1.0-2) ...
Selecting previously unselected package python3-tblib.
Preparing to unpack .../120-python3-tblib_1.7.0-2_all.deb ...
Unpacking python3-tblib (1.7.0-2) ...
Selecting previously unselected package python3-tornado.
Preparing to unpack .../121-python3-tornado_6.1.0-3build1_amd64.deb ...
Unpacking python3-tornado (6.1.0-3build1) ...
Selecting previously unselected package python3-heapdict.
Preparing to unpack .../122-python3-heapdict_1.0.1-1_all.deb ...
Unpacking python3-heapdict (1.0.1-1) ...
Selecting previously unselected package python3-zict.
Preparing to unpack .../123-python3-zict_2.0.0-1_all.deb ...
Unpacking python3-zict (2.0.0-1) ...
Selecting previously unselected package python3-distributed.
Preparing to unpack .../124-python3-distributed_2022.01.0+ds.1-1_all.deb ...
Unpacking python3-distributed (2022.01.0+ds.1-1) ...
Selecting previously unselected package python3-ply.
Preparing to unpack .../125-python3-ply_3.11-5_all.deb ...
Unpacking python3-ply (3.11-5) ...
Selecting previously unselected package python3-stone.
Preparing to unpack .../126-python3-stone_3.3.1-1_all.deb ...
Unpacking python3-stone (3.3.1-1) ...
Selecting previously unselected package python3-dropbox.
Preparing to unpack .../127-python3-dropbox_11.26.0-1_all.deb ...
Unpacking python3-dropbox (11.26.0-1) ...
Selecting previously unselected package python3-et-xmlfile.
Preparing to unpack .../128-python3-et-xmlfile_1.0.1-2.1_all.deb ...
Unpacking python3-et-xmlfile (1.0.1-2.1) ...
Selecting previously unselected package python3-pythran.
Preparing to unpack .../129-python3-pythran_0.10.0+ds2-1_amd64.deb ...
Unpacking python3-pythran (0.10.0+ds2-1) ...
Selecting previously unselected package python3-scipy.
Preparing to unpack .../130-python3-scipy_1.8.0-1exp2ubuntu1_amd64.deb ...
Unpacking python3-scipy (1.8.0-1exp2ubuntu1) ...
Selecting previously unselected package python3-ufolib2.
Preparing to unpack .../131-python3-ufolib2_0.13.1+dfsg1-1_all.deb ...
Unpacking python3-ufolib2 (0.13.1+dfsg1-1) ...
Selecting previously unselected package python3-mpmath.
Preparing to unpack .../132-python3-mpmath_1.2.1-2_all.deb ...
Unpacking python3-mpmath (1.2.1-2) ...
Selecting previously unselected package python3-sympy.
Preparing to unpack .../133-python3-sympy_1.9-1_all.deb ...
Unpacking python3-sympy (1.9-1) ...
Selecting previously unselected package python3-fs.
Preparing to unpack .../134-python3-fs_2.4.12-1_all.deb ...
Unpacking python3-fs (2.4.12-1) ...
Selecting previously unselected package python3-lxml:amd64.
Preparing to unpack .../135-python3-lxml_4.8.0-1build1_amd64.deb ...
Unpacking python3-lxml:amd64 (4.8.0-1build1) ...
Selecting previously unselected package python3-lz4.
Preparing to unpack .../136-python3-lz4_3.1.3+dfsg-1build3_amd64.deb ...
Unpacking python3-lz4 (3.1.3+dfsg-1build3) ...
Selecting previously unselected package python3-unicodedata2.
Preparing to unpack .../137-python3-unicodedata2_14.0.0+ds-8_amd64.deb ...
Unpacking python3-unicodedata2 (14.0.0+ds-8) ...
Selecting previously unselected package unicode-data.
Preparing to unpack .../138-unicode-data_14.0.0-1.1_all.deb ...
Unpacking unicode-data (14.0.0-1.1) ...
Selecting previously unselected package python3-fonttools.
Preparing to unpack .../139-python3-fonttools_4.29.1-2build1_amd64.deb ...
Unpacking python3-fonttools (4.29.1-2build1) ...
Selecting previously unselected package python3-fusepy.
Preparing to unpack .../140-python3-fusepy_3.0.1-2_all.deb ...
Unpacking python3-fusepy (3.0.1-2) ...
Selecting previously unselected package python3-h5py-serial.
Preparing to unpack .../141-python3-h5py-serial_3.6.0-2build1_amd64.deb ...
Unpacking python3-h5py-serial (3.6.0-2build1) ...
Selecting previously unselected package python3-h5netcdf.
Preparing to unpack .../142-python3-h5netcdf_0.12.0-1_all.deb ...
Unpacking python3-h5netcdf (0.12.0-1) ...
Selecting previously unselected package python3-webencodings.
Preparing to unpack .../143-python3-webencodings_0.5.1-4_all.deb ...
Unpacking python3-webencodings (0.5.1-4) ...
Selecting previously unselected package python3-html5lib.
Preparing to unpack .../144-python3-html5lib_1.1-3_all.deb ...
Unpacking python3-html5lib (1.1-3) ...
Selecting previously unselected package python3-iniconfig.
Preparing to unpack .../145-python3-iniconfig_1.1.1-2_all.deb ...
Unpacking python3-iniconfig (1.1.1-2) ...
Selecting previously unselected package python3-jdcal.
Preparing to unpack .../146-python3-jdcal_1.0-1.3_all.deb ...
Unpacking python3-jdcal (1.0-1.3) ...
Selecting previously unselected package python3-kiwisolver.
Preparing to unpack .../147-python3-kiwisolver_1.3.2-1build1_amd64.deb ...
Unpacking python3-kiwisolver (1.3.2-1build1) ...
Selecting previously unselected package python3-llvmlite.
Preparing to unpack .../148-python3-llvmlite_0.38.0-1_amd64.deb ...
Unpacking python3-llvmlite (0.38.0-1) ...
Selecting previously unselected package python3-tk:amd64.
Preparing to unpack .../149-python3-tk_3.10.6-1~22.04_amd64.deb ...
Unpacking python3-tk:amd64 (3.10.6-1~22.04) ...
Selecting previously unselected package python3-pil.imagetk:amd64.
Preparing to unpack .../150-python3-pil.imagetk_9.0.1-1ubuntu0.1_amd64.deb ...
Unpacking python3-pil.imagetk:amd64 (9.0.1-1ubuntu0.1) ...
Selecting previously unselected package python3-matplotlib.
Preparing to unpack .../151-python3-matplotlib_3.5.1-2build1_amd64.deb ...
Unpacking python3-matplotlib (3.5.1-2build1) ...
Selecting previously unselected package python3-netcdf4.
Preparing to unpack .../152-python3-netcdf4_1.5.8-1build1_amd64.deb ...
Unpacking python3-netcdf4 (1.5.8-1build1) ...
Selecting previously unselected package python3-numba.
Preparing to unpack .../153-python3-numba_0.55.1-0ubuntu2_amd64.deb ...
Unpacking python3-numba (0.55.1-0ubuntu2) ...
Selecting previously unselected package python3-numcodecs.
Preparing to unpack .../154-python3-numcodecs_0.9.1+ds-2build1_amd64.deb ...
Unpacking python3-numcodecs (0.9.1+ds-2build1) ...
Selecting previously unselected package python3-numexpr.
Preparing to unpack .../155-python3-numexpr_2.8.1-1build1_amd64.deb ...
Unpacking python3-numexpr (2.8.1-1build1) ...
Selecting previously unselected package python3-openpyxl.
Preparing to unpack .../156-python3-openpyxl_3.0.9-1_all.deb ...
Unpacking python3-openpyxl (3.0.9-1) ...
Selecting previously unselected package python3-pandas-lib:amd64.
Preparing to unpack .../157-python3-pandas-lib_1.3.5+dfsg-3_amd64.deb ...
Unpacking python3-pandas-lib:amd64 (1.3.5+dfsg-3) ...
Selecting previously unselected package python3-pandas.
Preparing to unpack .../158-python3-pandas_1.3.5+dfsg-3_all.deb ...
Unpacking python3-pandas (1.3.5+dfsg-3) ...
Selecting previously unselected package python3-pluggy.
Preparing to unpack .../159-python3-pluggy_0.13.0-7.1_all.deb ...
Unpacking python3-pluggy (0.13.0-7.1) ...
Selecting previously unselected package python3-py.
Preparing to unpack .../160-python3-py_1.10.0-1_all.deb ...
Unpacking python3-py (1.10.0-1) ...
Selecting previously unselected package python3-pygit2.
Preparing to unpack .../161-python3-pygit2_1.6.1+dfsg-2_amd64.deb ...
Unpacking python3-pygit2 (1.6.1+dfsg-2) ...
Selecting previously unselected package python3-toml.
Preparing to unpack .../162-python3-toml_0.10.2-1_all.deb ...
Unpacking python3-toml (0.10.2-1) ...
Selecting previously unselected package python3-pytest.
Preparing to unpack .../163-python3-pytest_6.2.5-1ubuntu2_all.deb ...
Unpacking python3-pytest (6.2.5-1ubuntu2) ...
Selecting previously unselected package python3-tables-lib.
Preparing to unpack .../164-python3-tables-lib_3.7.0-2build1_amd64.deb ...
Unpacking python3-tables-lib (3.7.0-2build1) ...
Selecting previously unselected package python3-tables.
Preparing to unpack .../165-python3-tables_3.7.0-2build1_all.deb ...
Unpacking python3-tables (3.7.0-2build1) ...
Selecting previously unselected package python3-xarray.
Preparing to unpack .../166-python3-xarray_0.21.1-1_all.deb ...
Unpacking python3-xarray (0.21.1-1) ...
Selecting previously unselected package python3-xlwt.
Preparing to unpack .../167-python3-xlwt_1.3.0-3_all.deb ...
Unpacking python3-xlwt (1.3.0-3) ...
Selecting previously unselected package python3-zarr.
Preparing to unpack .../168-python3-zarr_2.10.3+ds-1_all.deb ...
Unpacking python3-zarr (2.10.3+ds-1) ...
Selecting previously unselected package python3-zmq.
Preparing to unpack .../169-python3-zmq_22.3.0-1build1_amd64.deb ...
Unpacking python3-zmq (22.3.0-1build1) ...
Selecting previously unselected package qt5-gtk-platformtheme:amd64.
Preparing to unpack .../170-qt5-gtk-platformtheme_5.15.3+dfsg-2ubuntu0.2_amd64.deb ...
Unpacking qt5-gtk-platformtheme:amd64 (5.15.3+dfsg-2ubuntu0.2) ...
Selecting previously unselected package qttranslations5-l10n.
Preparing to unpack .../171-qttranslations5-l10n_5.15.3-1_all.deb ...
Unpacking qttranslations5-l10n (5.15.3-1) ...
Selecting previously unselected package python3-cdo.
Preparing to unpack .../172-python3-cdo_1.5.6-1_amd64.deb ...
Unpacking python3-cdo (1.5.6-1) ...
Selecting previously unselected package python3-libarchive-c.
Preparing to unpack .../173-python3-libarchive-c_2.9-0.1_all.deb ...
Unpacking python3-libarchive-c (2.9-0.1) ...
Setting up python3-heapdict (1.0.1-1) ...
Setting up python3-iniconfig (1.1.1-2) ...
Setting up libtbbmalloc2:amd64 (2021.5.0-7ubuntu2) ...
Setting up python3-attr (21.2.0-1) ...
Setting up python3-tornado (6.1.0-3build1) ...
Setting up mysql-common (5.8+1.0.8) ...
update-alternatives: using /etc/mysql/my.cnf.fallback to provide /etc/mysql/my.cnf (my.cnf) in auto mode
Setting up libibverbs1:amd64 (39.0-1) ...
Setting up libmysqlclient21:amd64 (8.0.32-0ubuntu0.22.04.2) ...
Setting up libdouble-conversion3:amd64 (3.1.7-4) ...
Setting up tk8.6-blt2.5 (2.5.3+dfsg-4.1build2) ...
Setting up libncurses-dev:amd64 (6.3-2) ...
Setting up libboost1.74-dev:amd64 (1.74.0-14ubuntu3) ...
Setting up fonts-lato (2.0-2.1) ...
Setting up python3-libarchive-c (2.9-0.1) ...
Setting up libopenblas0-pthread:amd64 (0.3.20+ds-1) ...
update-alternatives: using /usr/lib/x86_64-linux-gnu/openblas-pthread/libblas.so.3 to provide /usr/lib/x86_64-linux-gnu/libblas.so.3 (libblas.so.3-x86_64-linux-gnu) in auto mode
update-alternatives: using /usr/lib/x86_64-linux-gnu/openblas-pthread/liblapack.so.3 to provide /usr/lib/x86_64-linux-gnu/liblapack.so.3 (liblapack.so.3-x86_64-linux-gnu) in auto mode
update-alternatives: using /usr/lib/x86_64-linux-gnu/openblas-pthread/libopenblas.so.0 to provide /usr/lib/x86_64-linux-gnu/libopenblas.so.0 (libopenblas.so.0-x86_64-linux-gnu) in auto mode
Setting up libxcb-xinput0:amd64 (1.14-3ubuntu3) ...
Setting up python3-tblib (1.7.0-2) ...
Setting up python3-py (1.10.0-1) ...
Setting up python3-jdcal (1.0-1.3) ...
Setting up ibverbs-providers:amd64 (39.0-1) ...
Setting up python3-lz4 (3.1.3+dfsg-1build3) ...
Setting up python3-defusedxml (0.7.1-1) ...
Setting up python3-unicodedata2 (14.0.0+ds-8) ...
Setting up fonts-lyx (2.3.6-1) ...
Setting up blt (2.5.3+dfsg-4.1build2) ...
Setting up python3-fsspec (2022.01.0-1) ...
Setting up python3-ply (3.11-5) ...
Setting up python3-gast (0.5.2-2) ...
Setting up libpq5:amd64 (14.6-0ubuntu0.22.04.1) ...
Setting up libeccodes-data (2.24.2-1) ...
Setting up libqhull-r8.0:amd64 (2020.2-4) ...
Setting up python3-tk:amd64 (3.10.6-1~22.04) ...
Setting up libdxflib3:amd64 (3.26.4-1) ...
Setting up libtbb12:amd64 (2021.5.0-7ubuntu2) ...
Setting up python3-sortedcontainers (2.1.0-2) ...
Setting up libfuse2:amd64 (2.9.9-5ubuntu3) ...
Setting up libffi-dev:amd64 (3.4.2-4) ...
Setting up python3-webencodings (0.5.1-4) ...
Setting up libpcre2-16-0:amd64 (10.39-3ubuntu0.1) ...
Setting up python3-psutil (5.9.0-1build1) ...
Setting up libmagics++-data (4.10.1-1) ...
Setting up python-babel-localedata (2.8.0+dfsg.1-7) ...
Setting up libgeotiff5:amd64 (1.7.0-2build1) ...
Setting up python3-cloudpickle (2.0.0-1) ...
Setting up libxnvctrl0:amd64 (510.47.03-0ubuntu1) ...
Setting up unicode-data (14.0.0-1.1) ...
Setting up python3-beniget (0.4.1-2) ...
Setting up python3-stone (3.3.1-1) ...
Setting up libxsimd-dev:amd64 (7.6.0-2) ...
Setting up python3-decorator (4.4.2-0ubuntu1) ...
Setting up python3-pygments (2.11.2+dfsg-2) ...
Setting up libz3-4:amd64 (4.8.12-1) ...
Setting up python3-packaging (21.3-1) ...
Setting up libxcb-xinerama0:amd64 (1.14-3ubuntu3) ...
Setting up libpfm4:amd64 (4.11.1+git32-gd0b85fb-1ubuntu0.1) ...
Setting up libllvm11:amd64 (1:11.1.0-6) ...
Setting up libjs-jquery-ui (1.13.1+dfsg-1) ...
Setting up qttranslations5-l10n (5.15.3-1) ...
Setting up libmbedcrypto7:amd64 (2.28.0-1build1) ...
Setting up python3-pil.imagetk:amd64 (9.0.1-1ubuntu0.1) ...
Setting up python3-zmq (22.3.0-1build1) ...
Setting up python3-brotli (1.0.9-2build6) ...
Setting up liblzf1:amd64 (3.6-3) ...
Setting up python3-cycler (0.11.0-1) ...
Setting up python-odf-doc (1.4.2-1) ...
Setting up python3-kiwisolver (1.3.2-1build1) ...
Setting up libhwloc15:amd64 (2.7.0-2ubuntu1) ...
Setting up python3-xlwt (1.3.0-3) ...
Setting up libevent-core-2.1-7:amd64 (2.1.12-stable-1build3) ...
Setting up binfmt-support (2.2.1-2) ...
Created symlink /etc/systemd/system/multi-user.target.wants/binfmt-support.service → /lib/systemd/system/binfmt-support.service.
Setting up icu-devtools (70.1-2) ...
Setting up libeccodes0:amd64 (2.24.2-1) ...
Setting up python3-asciitree (0.3.3-3) ...
Setting up libqt5core5a:amd64 (5.15.3+dfsg-2ubuntu0.2) ...
Setting up python3-html5lib (1.1-3) ...
Setting up python3-numpy (1:1.21.5-1ubuntu22.04.1) ...
Setting up libfftw3-double3:amd64 (3.3.8-2ubuntu8) ...
Setting up python3-toml (0.10.2-1) ...
Setting up python3-pluggy (0.13.0-7.1) ...
Setting up llvm-11-linker-tools (1:11.1.0-6) ...
Setting up fonts-dejavu-extra (2.37-2build1) ...
Setting up libopenblas0:amd64 (0.3.20+ds-1) ...
Setting up python3-lxml:amd64 (4.8.0-1build1) ...
Setting up libqt5dbus5:amd64 (5.15.3+dfsg-2ubuntu0.2) ...
Setting up libblosc1:amd64 (1.21.1+ds2-2) ...
Setting up python3-et-xmlfile (1.0.1-2.1) ...
Setting up libpsm2-2 (11.2.185-1) ...
Setting up libmd4c0:amd64 (0.4.8-1) ...
Setting up python3-toolz (0.11.2-1) ...
Setting up libssh2-1:amd64 (1.10.0-3) ...
Setting up python3-msgpack (1.0.3-1build1) ...
Setting up libboost-dev:amd64 (1.74.0.3ubuntu7) ...
Setting up libpsm-infinipath1 (3.3+20.604758e7-6.1) ...
update-alternatives: using /usr/lib/libpsm1/libpsm_infinipath.so.1.16 to provide /usr/lib/x86_64-linux-gnu/libpsm_infinipath.so.1 (libpsm_infinipath.so.1) in auto mode
Setting up python3-mpmath (1.2.1-2) ...
Setting up python3-zict (2.0.0-1) ...
Setting up python-matplotlib-data (3.5.1-2build1) ...
Setting up python3-locket (0.2.1-1) ...
Setting up python3-appdirs (1.4.4-2) ...
Setting up libicu-dev:amd64 (70.1-2) ...
Setting up python3-soupsieve (2.3.1-1) ...
Setting up python-tables-data (3.7.0-2build1) ...
Setting up fonts-font-awesome (5.0.10+really4.7.0~dfsg-4.1) ...
Setting up sphinx-rtd-theme-common (1.0.0+dfsg-1) ...
Setting up libhttp-parser2.9:amd64 (2.9.4-4) ...
Setting up liblbfgsb0:amd64 (3.0+dfsg.3-10) ...
Setting up python3-odf (1.4.2-1) ...
Setting up libevent-pthreads-2.1-7:amd64 (2.1.12-stable-1build3) ...
Setting up python3-dropbox (11.26.0-1) ...
Setting up libopenblas-pthread-dev:amd64 (0.3.20+ds-1) ...
update-alternatives: using /usr/lib/x86_64-linux-gnu/openblas-pthread/libblas.so to provide /usr/lib/x86_64-linux-gnu/libblas.so (libblas.so-x86_64-linux-gnu) in auto mode
update-alternatives: using /usr/lib/x86_64-linux-gnu/openblas-pthread/liblapack.so to provide /usr/lib/x86_64-linux-gnu/liblapack.so (liblapack.so-x86_64-linux-gnu) in auto mode
update-alternatives: using /usr/lib/x86_64-linux-gnu/openblas-pthread/libopenblas.so to provide /usr/lib/x86_64-linux-gnu/libopenblas.so (libopenblas.so-x86_64-linux-gnu) in auto mode
Setting up python3-partd (1.2.0-1) ...
Setting up python3-sympy (1.9-1) ...
Setting up librdmacm1:amd64 (39.0-1) ...
Setting up libtinfo-dev:amd64 (6.3-2) ...
Setting up libz3-dev:amd64 (4.8.12-1) ...
Setting up libucx0:amd64 (1.12.1~rc2-1) ...
Setting up llvm-11-runtime (1:11.1.0-6) ...
Setting up libmbedx509-1:amd64 (2.28.0-1build1) ...
Setting up libmbedtls14:amd64 (2.28.0-1build1) ...
Setting up python3-babel (2.8.0+dfsg.1-7) ...
update-alternatives: using /usr/bin/pybabel-python3 to provide /usr/bin/pybabel (pybabel) in auto mode
Setting up libgit2-1.1:amd64 (1.1.0+dfsg.1-4.1build1) ...
Setting up llvm-11-tools (1:11.1.0-6) ...
Setting up python3-pygit2 (1.6.1+dfsg-2) ...
Setting up python3-pytest (6.2.5-1ubuntu2) ...
Setting up python3-tables-lib (3.7.0-2build1) ...
Setting up python3-numcodecs (0.9.1+ds-2build1) ...
Setting up python3-pandas-lib:amd64 (1.3.5+dfsg-3) ...
Setting up libcdi0:amd64 (2.0.4-1) ...
Setting up python-odf-tools (1.4.2-1) ...
Setting up libterralib3:amd64 (4.3.0+dfsg.2-12.1build2) ...
Setting up python3-dask (2022.01.0+dfsg-1ubuntu1) ...
Setting up python3-h5py-serial (3.6.0-2build1) ...
Setting up llvm-11 (1:11.1.0-6) ...
Setting up python3-fusepy (3.0.1-2) ...
Setting up libhwloc-plugins:amd64 (2.7.0-2ubuntu1) ...
Setting up libqt5network5:amd64 (5.15.3+dfsg-2ubuntu0.2) ...
Setting up python3-bs4 (4.10.0-2) ...
Setting up python3-fs (2.4.12-1) ...
Setting up python3-blosc (1.9.2+ds1-3build2) ...
Setting up libclang-cpp11 (1:11.1.0-6) ...
Setting up python3-llvmlite (0.38.0-1) ...
Setting up libopenblas-dev:amd64 (0.3.20+ds-1) ...
Setting up python3-jinja2 (3.0.3-1) ...
Setting up libxml2-dev:amd64 (2.9.13+dfsg-1ubuntu0.2) ...
Setting up python3-distributed (2022.01.0+ds.1-1) ...
Setting up python3-h5netcdf (0.12.0-1) ...
Setting up python3-pandas (1.3.5+dfsg-3) ...
Setting up python3-openpyxl (3.0.9-1) ...
Setting up python3-bottleneck (1.3.2+ds1-2build1) ...
Setting up python3-cftime (1.5.2+ds-1build1) ...
Setting up python3-numexpr (2.8.1-1build1) ...
Setting up python3-pythran (0.10.0+ds2-1) ...
Setting up numba-doc (0.55.1-0ubuntu2) ...
Setting up python3-zarr (2.10.3+ds-1) ...
Setting up python3-netcdf4 (1.5.8-1build1) ...
Setting up libfabric1:amd64 (1.11.0-3) ...
Setting up python3-scipy (1.8.0-1exp2ubuntu1) ...
Setting up llvm-11-dev (1:11.1.0-6) ...
Setting up libpmix2:amd64 (4.1.2-2ubuntu1) ...
Setting up libopenmpi3:amd64 (4.1.2-2ubuntu1) ...
Setting up python3-xarray (0.21.1-1) ...
Setting up libqt5gui5:amd64 (5.15.3+dfsg-2ubuntu0.2) ...
Setting up libqt5widgets5:amd64 (5.15.3+dfsg-2ubuntu0.2) ...
Setting up python3-tables (3.7.0-2build1) ...
Setting up python3-numba (0.55.1-0ubuntu2) ...
update-alternatives: using /usr/share/python3-numba/numba to provide /usr/bin/numba (numba) in auto mode
Setting up qt5-gtk-platformtheme:amd64 (5.15.3+dfsg-2ubuntu0.2) ...
Setting up libeckit0d:amd64 (1.18.7-1) ...
Setting up libqt5svg5:amd64 (5.15.3-1) ...
Setting up libodc-0d:amd64 (1.4.4-1) ...
Setting up libmagplus3v5:amd64 (4.10.1-1) ...
Setting up cdo (2.0.4-1) ...
Setting up python3-cdo (1.5.6-1) ...
Setting up python3-ufolib2 (0.13.1+dfsg1-1) ...
Setting up python3-fonttools (4.29.1-2build1) ...
Setting up python3-matplotlib (3.5.1-2build1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.1) ...
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for install-info (6.8-4build1) ...
Processing triggers for fontconfig (2.13.1-4.2ubuntu5) ...
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo sinfo air.mon.ltm.nc 
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
   File format : NetCDF4 classic zip
    -1 : Institut Source   T Steptype Levels Num    Points Num Dtype : Parameter ID
     1 : NCEP     NCEP/DOE v instant      17   1     10512   1  F32z : -1            
     2 : NCEP     NCEP/DOE v instant      17   1     10512   1  I16  : -2            
   Grid coordinates :
     1 : lonlat                   : points=10512 (144x73)
                              lon : 0 to 357.5 by 2.5 degrees_east  circular
                              lat : 90 to -90 by -2.5 degrees_north
   Vertical coordinates :
     1 : pressure                 : levels=17
                            level : 1000 to 10 millibar
   Time coordinate :
                             time : 12 steps
     RefTime =  1800-01-01 00:00:00  Units = hours  Calendar = standard  Bounds = true
  YYYY-MM-DD hh:mm:ss  YYYY-MM-DD hh:mm:ss  YYYY-MM-DD hh:mm:ss  YYYY-MM-DD hh:mm:ss
  0001-01-01 00:00:00  0001-02-01 00:00:00  0001-03-01 00:00:00  0001-04-01 00:00:00
  0001-05-01 00:00:00  0001-06-01 00:00:00  0001-07-01 00:00:00  0001-08-01 00:00:00
  0001-09-01 00:00:00  0001-10-01 00:00:00  0001-11-01 00:00:00  0001-12-01 00:00:00
cdo    sinfo: Processed 2 variables over 12 timesteps [0.02s 46MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo info air.mon.ltm.nc 
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
    -1 :       Date     Time   Level Gridsize    Miss :     Minimum        Mean     Maximum : Parameter ID
     1 : 0001-01-01 00:00:00    1000    10512       0 :      244.25      279.68      308.67 : -1            
     2 : 0001-01-01 00:00:00     925    10512       0 :      244.56      276.17      303.57 : -1            
     3 : 0001-01-01 00:00:00     850    10512       0 :      247.07      273.46      297.96 : -1            
     4 : 0001-01-01 00:00:00     700    10512       0 :      245.16      266.39      284.88 : -1            
     5 : 0001-01-01 00:00:00     600    10512       0 :      239.81      260.13      277.66 : -1            
     6 : 0001-01-01 00:00:00     500    10512       0 :      232.17      251.66      268.99 : -1            
     7 : 0001-01-01 00:00:00     400    10512       0 :      222.35      241.23      258.82 : -1            
     8 : 0001-01-01 00:00:00     300    10512       0 :      212.77      229.50      244.29 : -1            
     9 : 0001-01-01 00:00:00     250    10512       0 :      210.36      224.09      234.37 : -1            
    10 : 0001-01-01 00:00:00     200    10512       0 :      209.07      219.68      227.75 : -1            
    11 : 0001-01-01 00:00:00     150    10512       0 :      205.56      215.25      230.66 : -1            
    12 : 0001-01-01 00:00:00     100    10512       0 :      190.07      210.29      231.98 : -1            
    13 : 0001-01-01 00:00:00      70    10512       0 :      193.78      210.66      234.17 : -1            
    14 : 0001-01-01 00:00:00      50    10512       0 :      198.20      213.72      235.77 : -1            
    15 : 0001-01-01 00:00:00      30    10512       0 :      197.87      218.36      237.98 : -1            
    16 : 0001-01-01 00:00:00      20    10512       0 :      199.96      222.39      240.74 : -1            
    17 : 0001-01-01 00:00:00      10    10512       0 :      206.35      230.12      248.99 : -1            
    18 : 0001-01-01 00:00:00    1000    10512       0 :      30.000      30.000      30.000 : -2            
    19 : 0001-01-01 00:00:00     925    10512       0 :      30.000      30.000      30.000 : -2            
    20 : 0001-01-01 00:00:00     850    10512       0 :      30.000      30.000      30.000 : -2            
    21 : 0001-01-01 00:00:00     700    10512       0 :      30.000      30.000      30.000 : -2            
    22 : 0001-01-01 00:00:00     600    10512       0 :      30.000      30.000      30.000 : -2            
    23 : 0001-01-01 00:00:00     500    10512       0 :      30.000      30.000      30.000 : -2            
    24 : 0001-01-01 00:00:00     400    10512       0 :      30.000      30.000      30.000 : -2            
    25 : 0001-01-01 00:00:00     300    10512       0 :      30.000      30.000      30.000 : -2            
    26 : 0001-01-01 00:00:00     250    10512       0 :      30.000      30.000      30.000 : -2            
    27 : 0001-01-01 00:00:00     200    10512       0 :      30.000      30.000      30.000 : -2            
    28 : 0001-01-01 00:00:00     150    10512       0 :      30.000      30.000      30.000 : -2            
    29 : 0001-01-01 00:00:00     100    10512       0 :      30.000      30.000      30.000 : -2            
    30 : 0001-01-01 00:00:00      70    10512       0 :      30.000      30.000      30.000 : -2            
    31 : 0001-01-01 00:00:00      50    10512       0 :      30.000      30.000      30.000 : -2            
    32 : 0001-01-01 00:00:00      30    10512       0 :      30.000      30.000      30.000 : -2            
    33 : 0001-01-01 00:00:00      20    10512       0 :      30.000      30.000      30.000 : -2            
    34 : 0001-01-01 00:00:00      10    10512       0 :      30.000      30.000      30.000 : -2            
    35 : 0001-02-01 00:00:00    1000    10512       0 :      244.26      279.23      307.21 : -1            
    36 : 0001-02-01 00:00:00     925    10512       0 :      245.69      275.71      302.47 : -1            
    37 : 0001-02-01 00:00:00     850    10512       0 :      247.06      272.90      297.53 : -1            
    38 : 0001-02-01 00:00:00     700    10512       0 :      238.00      265.87      284.74 : -1            
    39 : 0001-02-01 00:00:00     600    10512       0 :      234.44      259.89      277.59 : -1            
    40 : 0001-02-01 00:00:00     500    10512       0 :      231.96      251.60      269.10 : -1            
    41 : 0001-02-01 00:00:00     400    10512       0 :      222.17      241.25      258.89 : -1            
    42 : 0001-02-01 00:00:00     300    10512       0 :      213.52      229.69      244.37 : -1            
    43 : 0001-02-01 00:00:00     250    10512       0 :      211.31      224.45      234.46 : -1            
    44 : 0001-02-01 00:00:00     200    10512       0 :      210.80      220.17      228.23 : -1            
    45 : 0001-02-01 00:00:00     150    10512       0 :      205.53      215.66      231.02 : -1            
    46 : 0001-02-01 00:00:00     100    10512       0 :      190.48      210.48      230.08 : -1            
    47 : 0001-02-01 00:00:00      70    10512       0 :      194.14      210.69      230.86 : -1            
    48 : 0001-02-01 00:00:00      50    10512       0 :      202.41      213.64      231.48 : -1            
    49 : 0001-02-01 00:00:00      30    10512       0 :      203.19      218.19      232.47 : -1            
    50 : 0001-02-01 00:00:00      20    10512       0 :      205.22      222.10      234.09 : -1            
    51 : 0001-02-01 00:00:00      10    10512       0 :      211.22      229.46      240.03 : -1            
    52 : 0001-02-01 00:00:00    1000    10512       0 :      30.000      30.000      30.000 : -2            
    53 : 0001-02-01 00:00:00     925    10512       0 :      30.000      30.000      30.000 : -2            
    54 : 0001-02-01 00:00:00     850    10512       0 :      30.000      30.000      30.000 : -2            
    55 : 0001-02-01 00:00:00     700    10512       0 :      30.000      30.000      30.000 : -2            
    56 : 0001-02-01 00:00:00     600    10512       0 :      30.000      30.000      30.000 : -2            
    57 : 0001-02-01 00:00:00     500    10512       0 :      30.000      30.000      30.000 : -2            
    58 : 0001-02-01 00:00:00     400    10512       0 :      30.000      30.000      30.000 : -2            
    59 : 0001-02-01 00:00:00     300    10512       0 :      30.000      30.000      30.000 : -2            
    60 : 0001-02-01 00:00:00     250    10512       0 :      30.000      30.000      30.000 : -2            
    61 : 0001-02-01 00:00:00     200    10512       0 :      30.000      30.000      30.000 : -2            
    62 : 0001-02-01 00:00:00     150    10512       0 :      30.000      30.000      30.000 : -2            
    63 : 0001-02-01 00:00:00     100    10512       0 :      30.000      30.000      30.000 : -2            
    64 : 0001-02-01 00:00:00      70    10512       0 :      30.000      30.000      30.000 : -2            
    65 : 0001-02-01 00:00:00      50    10512       0 :      30.000      30.000      30.000 : -2            
    66 : 0001-02-01 00:00:00      30    10512       0 :      30.000      30.000      30.000 : -2            
    67 : 0001-02-01 00:00:00      20    10512       0 :      30.000      30.000      30.000 : -2            
    68 : 0001-02-01 00:00:00      10    10512       0 :      30.000      30.000      30.000 : -2            
    69 : 0001-03-01 00:00:00    1000    10512       0 :      245.45      279.24      307.91 : -1            
    70 : 0001-03-01 00:00:00     925    10512       0 :      242.03      275.66      303.62 : -1            
    71 : 0001-03-01 00:00:00     850    10512       0 :      238.15      272.66      298.63 : -1            
    72 : 0001-03-01 00:00:00     700    10512       0 :      229.38      265.47      285.29 : -1            
    73 : 0001-03-01 00:00:00     600    10512       0 :      225.98      259.59      277.35 : -1            
    74 : 0001-03-01 00:00:00     500    10512       0 :      231.29      251.42      268.96 : -1            
    75 : 0001-03-01 00:00:00     400    10512       0 :      223.39      241.11      258.75 : -1            
    76 : 0001-03-01 00:00:00     300    10512       0 :      214.90      229.49      244.08 : -1            
    77 : 0001-03-01 00:00:00     250    10512       0 :      212.87      224.13      233.91 : -1            
    78 : 0001-03-01 00:00:00     200    10512       0 :      212.65      219.82      226.07 : -1            
    79 : 0001-03-01 00:00:00     150    10512       0 :      205.87      215.38      227.49 : -1            
    80 : 0001-03-01 00:00:00     100    10512       0 :      191.14      210.26      225.75 : -1            
    81 : 0001-03-01 00:00:00      70    10512       0 :      195.22      210.41      224.80 : -1            
    82 : 0001-03-01 00:00:00      50    10512       0 :      203.62      213.14      224.12 : -1            
    83 : 0001-03-01 00:00:00      30    10512       0 :      210.09      217.34      224.83 : -1            
    84 : 0001-03-01 00:00:00      20    10512       0 :      211.82      220.94      226.34 : -1            
    85 : 0001-03-01 00:00:00      10    10512       0 :      215.93      227.64      232.44 : -1            
    86 : 0001-03-01 00:00:00    1000    10512       0 :      30.000      30.000      30.000 : -2            
    87 : 0001-03-01 00:00:00     925    10512       0 :      30.000      30.000      30.000 : -2            
    88 : 0001-03-01 00:00:00     850    10512       0 :      30.000      30.000      30.000 : -2            
    89 : 0001-03-01 00:00:00     700    10512       0 :      30.000      30.000      30.000 : -2            
    90 : 0001-03-01 00:00:00     600    10512       0 :      30.000      30.000      30.000 : -2            
    91 : 0001-03-01 00:00:00     500    10512       0 :      30.000      30.000      30.000 : -2            
    92 : 0001-03-01 00:00:00     400    10512       0 :      30.000      30.000      30.000 : -2            
    93 : 0001-03-01 00:00:00     300    10512       0 :      30.000      30.000      30.000 : -2            
    94 : 0001-03-01 00:00:00     250    10512       0 :      30.000      30.000      30.000 : -2            
    95 : 0001-03-01 00:00:00     200    10512       0 :      30.000      30.000      30.000 : -2            
    96 : 0001-03-01 00:00:00     150    10512       0 :      30.000      30.000      30.000 : -2            
    97 : 0001-03-01 00:00:00     100    10512       0 :      30.000      30.000      30.000 : -2            
    98 : 0001-03-01 00:00:00      70    10512       0 :      30.000      30.000      30.000 : -2            
    99 : 0001-03-01 00:00:00      50    10512       0 :      30.000      30.000      30.000 : -2            
   100 : 0001-03-01 00:00:00      30    10512       0 :      30.000      30.000      30.000 : -2            
   101 : 0001-03-01 00:00:00      20    10512       0 :      30.000      30.000      30.000 : -2            
   102 : 0001-03-01 00:00:00      10    10512       0 :      30.000      30.000      30.000 : -2            
   103 : 0001-04-01 00:00:00    1000    10512       0 :      241.49      280.40      309.19 : -1            
   104 : 0001-04-01 00:00:00     925    10512       0 :      238.14      276.70      305.33 : -1            
   105 : 0001-04-01 00:00:00     850    10512       0 :      234.64      273.52      299.70 : -1            
   106 : 0001-04-01 00:00:00     700    10512       0 :      225.72      266.01      285.90 : -1            
   107 : 0001-04-01 00:00:00     600    10512       0 :      222.96      260.06      277.31 : -1            
   108 : 0001-04-01 00:00:00     500    10512       0 :      229.32      251.86      268.93 : -1            
   109 : 0001-04-01 00:00:00     400    10512       0 :      222.42      241.43      258.60 : -1            
   110 : 0001-04-01 00:00:00     300    10512       0 :      214.74      229.44      243.91 : -1            
   111 : 0001-04-01 00:00:00     250    10512       0 :      214.08      223.84      233.66 : -1            
   112 : 0001-04-01 00:00:00     200    10512       0 :      212.96      219.39      224.52 : -1            
   113 : 0001-04-01 00:00:00     150    10512       0 :      206.28      215.08      224.44 : -1            
   114 : 0001-04-01 00:00:00     100    10512       0 :      191.45      210.15      223.67 : -1            
   115 : 0001-04-01 00:00:00      70    10512       0 :      195.35      210.24      223.38 : -1            
   116 : 0001-04-01 00:00:00      50    10512       0 :      204.34      212.76      223.36 : -1            
   117 : 0001-04-01 00:00:00      30    10512       0 :      206.10      216.61      224.47 : -1            
   118 : 0001-04-01 00:00:00      20    10512       0 :      206.05      219.96      226.59 : -1            
   119 : 0001-04-01 00:00:00      10    10512       0 :      207.68      226.24      233.08 : -1            
   120 : 0001-04-01 00:00:00    1000    10512       0 :      30.000      30.000      30.000 : -2            
   121 : 0001-04-01 00:00:00     925    10512       0 :      30.000      30.000      30.000 : -2            
   122 : 0001-04-01 00:00:00     850    10512       0 :      30.000      30.000      30.000 : -2            
   123 : 0001-04-01 00:00:00     700    10512       0 :      30.000      30.000      30.000 : -2            
   124 : 0001-04-01 00:00:00     600    10512       0 :      30.000      30.000      30.000 : -2            
   125 : 0001-04-01 00:00:00     500    10512       0 :      30.000      30.000      30.000 : -2            
   126 : 0001-04-01 00:00:00     400    10512       0 :      30.000      30.000      30.000 : -2            
   127 : 0001-04-01 00:00:00     300    10512       0 :      30.000      30.000      30.000 : -2            
   128 : 0001-04-01 00:00:00     250    10512       0 :      30.000      30.000      30.000 : -2            
   129 : 0001-04-01 00:00:00     200    10512       0 :      30.000      30.000      30.000 : -2            
   130 : 0001-04-01 00:00:00     150    10512       0 :      30.000      30.000      30.000 : -2            
   131 : 0001-04-01 00:00:00     100    10512       0 :      30.000      30.000      30.000 : -2            
   132 : 0001-04-01 00:00:00      70    10512       0 :      30.000      30.000      30.000 : -2            
   133 : 0001-04-01 00:00:00      50    10512       0 :      30.000      30.000      30.000 : -2            
   134 : 0001-04-01 00:00:00      30    10512       0 :      30.000      30.000      30.000 : -2            
   135 : 0001-04-01 00:00:00      20    10512       0 :      30.000      30.000      30.000 : -2            
   136 : 0001-04-01 00:00:00      10    10512       0 :      30.000      30.000      30.000 : -2            
   137 : 0001-05-01 00:00:00    1000    10512       0 :      239.99      281.99      311.40 : -1            
   138 : 0001-05-01 00:00:00     925    10512       0 :      236.62      278.16      306.77 : -1            
   139 : 0001-05-01 00:00:00     850    10512       0 :      233.20      274.87      301.29 : -1            
   140 : 0001-05-01 00:00:00     700    10512       0 :      224.00      267.19      287.01 : -1            
   141 : 0001-05-01 00:00:00     600    10512       0 :      221.88      261.13      277.27 : -1            
   142 : 0001-05-01 00:00:00     500    10512       0 :      228.08      252.81      269.40 : -1            
   143 : 0001-05-01 00:00:00     400    10512       0 :      220.59      242.24      259.14 : -1            
   144 : 0001-05-01 00:00:00     300    10512       0 :      211.54      229.81      244.94 : -1            
   145 : 0001-05-01 00:00:00     250    10512       0 :      208.86      223.85      235.05 : -1            
   146 : 0001-05-01 00:00:00     200    10512       0 :      208.72      219.05      228.38 : -1            
   147 : 0001-05-01 00:00:00     150    10512       0 :      206.25      214.57      227.92 : -1            
   148 : 0001-05-01 00:00:00     100    10512       0 :      191.85      209.68      228.06 : -1            
   149 : 0001-05-01 00:00:00      70    10512       0 :      195.37      209.72      228.01 : -1            
   150 : 0001-05-01 00:00:00      50    10512       0 :      195.64      212.10      228.40 : -1            
   151 : 0001-05-01 00:00:00      30    10512       0 :      193.36      215.65      229.26 : -1            
   152 : 0001-05-01 00:00:00      20    10512       0 :      193.91      218.91      231.10 : -1            
   153 : 0001-05-01 00:00:00      10    10512       0 :      198.03      225.16      236.81 : -1            
   154 : 0001-05-01 00:00:00    1000    10512       0 :      30.000      30.000      30.000 : -2            
   155 : 0001-05-01 00:00:00     925    10512       0 :      30.000      30.000      30.000 : -2            
   156 : 0001-05-01 00:00:00     850    10512       0 :      30.000      30.000      30.000 : -2            
   157 : 0001-05-01 00:00:00     700    10512       0 :      30.000      30.000      30.000 : -2            
   158 : 0001-05-01 00:00:00     600    10512       0 :      30.000      30.000      30.000 : -2            
   159 : 0001-05-01 00:00:00     500    10512       0 :      30.000      30.000      30.000 : -2            
   160 : 0001-05-01 00:00:00     400    10512       0 :      30.000      30.000      30.000 : -2            
   161 : 0001-05-01 00:00:00     300    10512       0 :      30.000      30.000      30.000 : -2            
   162 : 0001-05-01 00:00:00     250    10512       0 :      30.000      30.000      30.000 : -2            
   163 : 0001-05-01 00:00:00     200    10512       0 :      30.000      30.000      30.000 : -2            
   164 : 0001-05-01 00:00:00     150    10512       0 :      30.000      30.000      30.000 : -2            
   165 : 0001-05-01 00:00:00     100    10512       0 :      30.000      30.000      30.000 : -2            
   166 : 0001-05-01 00:00:00      70    10512       0 :      30.000      30.000      30.000 : -2            
   167 : 0001-05-01 00:00:00      50    10512       0 :      30.000      30.000      30.000 : -2            
   168 : 0001-05-01 00:00:00      30    10512       0 :      30.000      30.000      30.000 : -2            
   169 : 0001-05-01 00:00:00      20    10512       0 :      30.000      30.000      30.000 : -2            
   170 : 0001-05-01 00:00:00      10    10512       0 :      30.000      30.000      30.000 : -2            
   171 : 0001-06-01 00:00:00    1000    10512       0 :      240.19      283.39      313.26 : -1            
   172 : 0001-06-01 00:00:00     925    10512       0 :      236.78      279.60      308.96 : -1            
   173 : 0001-06-01 00:00:00     850    10512       0 :      233.41      276.26      303.97 : -1            
   174 : 0001-06-01 00:00:00     700    10512       0 :      223.97      268.52      290.30 : -1            
   175 : 0001-06-01 00:00:00     600    10512       0 :      222.22      262.35      280.77 : -1            
   176 : 0001-06-01 00:00:00     500    10512       0 :      227.23      253.97      271.50 : -1            
   177 : 0001-06-01 00:00:00     400    10512       0 :      219.42      243.34      260.88 : -1            
   178 : 0001-06-01 00:00:00     300    10512       0 :      209.43      230.40      247.57 : -1            
   179 : 0001-06-01 00:00:00     250    10512       0 :      205.47      223.89      238.05 : -1            
   180 : 0001-06-01 00:00:00     200    10512       0 :      203.30      218.67      229.70 : -1            
   181 : 0001-06-01 00:00:00     150    10512       0 :      201.07      213.80      230.02 : -1            
   182 : 0001-06-01 00:00:00     100    10512       0 :      192.43      208.85      230.24 : -1            
   183 : 0001-06-01 00:00:00      70    10512       0 :      191.17      209.16      230.14 : -1            
   184 : 0001-06-01 00:00:00      50    10512       0 :      187.86      211.44      230.76 : -1            
   185 : 0001-06-01 00:00:00      30    10512       0 :      185.93      214.84      232.26 : -1            
   186 : 0001-06-01 00:00:00      20    10512       0 :      186.98      218.16      235.11 : -1            
   187 : 0001-06-01 00:00:00      10    10512       0 :      193.04      224.64      242.80 : -1            
   188 : 0001-06-01 00:00:00    1000    10512       0 :      30.000      30.000      30.000 : -2            
   189 : 0001-06-01 00:00:00     925    10512       0 :      30.000      30.000      30.000 : -2            
   190 : 0001-06-01 00:00:00     850    10512       0 :      30.000      30.000      30.000 : -2            
   191 : 0001-06-01 00:00:00     700    10512       0 :      30.000      30.000      30.000 : -2            
   192 : 0001-06-01 00:00:00     600    10512       0 :      30.000      30.000      30.000 : -2            
   193 : 0001-06-01 00:00:00     500    10512       0 :      30.000      30.000      30.000 : -2            
   194 : 0001-06-01 00:00:00     400    10512       0 :      30.000      30.000      30.000 : -2            
   195 : 0001-06-01 00:00:00     300    10512       0 :      30.000      30.000      30.000 : -2            
   196 : 0001-06-01 00:00:00     250    10512       0 :      30.000      30.000      30.000 : -2            
   197 : 0001-06-01 00:00:00     200    10512       0 :      30.000      30.000      30.000 : -2            
   198 : 0001-06-01 00:00:00     150    10512       0 :      30.000      30.000      30.000 : -2            
   199 : 0001-06-01 00:00:00     100    10512       0 :      30.000      30.000      30.000 : -2            
   200 : 0001-06-01 00:00:00      70    10512       0 :      30.000      30.000      30.000 : -2            
   201 : 0001-06-01 00:00:00      50    10512       0 :      30.000      30.000      30.000 : -2            
   202 : 0001-06-01 00:00:00      30    10512       0 :      30.000      30.000      30.000 : -2            
   203 : 0001-06-01 00:00:00      20    10512       0 :      30.000      30.000      30.000 : -2            
   204 : 0001-06-01 00:00:00      10    10512       0 :      30.000      30.000      30.000 : -2            
   205 : 0001-07-01 00:00:00    1000    10512       0 :      240.43      283.86      314.30 : -1            
   206 : 0001-07-01 00:00:00     925    10512       0 :      237.25      280.18      310.15 : -1            
   207 : 0001-07-01 00:00:00     850    10512       0 :      233.87      276.84      305.06 : -1            
   208 : 0001-07-01 00:00:00     700    10512       0 :      224.18      269.12      291.82 : -1            
   209 : 0001-07-01 00:00:00     600    10512       0 :      220.65      262.95      283.44 : -1            
   210 : 0001-07-01 00:00:00     500    10512       0 :      225.79      254.65      274.05 : -1            
   211 : 0001-07-01 00:00:00     400    10512       0 :      218.02      244.03      262.10 : -1            
   212 : 0001-07-01 00:00:00     300    10512       0 :      207.70      230.78      249.10 : -1            
   213 : 0001-07-01 00:00:00     250    10512       0 :      203.00      223.82      239.56 : -1            
   214 : 0001-07-01 00:00:00     200    10512       0 :      199.74      218.26      229.82 : -1            
   215 : 0001-07-01 00:00:00     150    10512       0 :      196.69      213.00      230.35 : -1            
   216 : 0001-07-01 00:00:00     100    10512       0 :      191.19      208.09      230.54 : -1            
   217 : 0001-07-01 00:00:00      70    10512       0 :      187.01      208.85      230.33 : -1            
   218 : 0001-07-01 00:00:00      50    10512       0 :      184.20      211.03      230.84 : -1            
   219 : 0001-07-01 00:00:00      30    10512       0 :      183.01      214.38      232.38 : -1            
   220 : 0001-07-01 00:00:00      20    10512       0 :      184.66      217.82      235.37 : -1            
   221 : 0001-07-01 00:00:00      10    10512       0 :      192.34      224.69      243.22 : -1            
   222 : 0001-07-01 00:00:00    1000    10512       0 :      30.000      30.000      30.000 : -2            
   223 : 0001-07-01 00:00:00     925    10512       0 :      30.000      30.000      30.000 : -2            
   224 : 0001-07-01 00:00:00     850    10512       0 :      30.000      30.000      30.000 : -2            
   225 : 0001-07-01 00:00:00     700    10512       0 :      30.000      30.000      30.000 : -2            
   226 : 0001-07-01 00:00:00     600    10512       0 :      30.000      30.000      30.000 : -2            
   227 : 0001-07-01 00:00:00     500    10512       0 :      30.000      30.000      30.000 : -2            
   228 : 0001-07-01 00:00:00     400    10512       0 :      30.000      30.000      30.000 : -2            
   229 : 0001-07-01 00:00:00     300    10512       0 :      30.000      30.000      30.000 : -2            
   230 : 0001-07-01 00:00:00     250    10512       0 :      30.000      30.000      30.000 : -2            
   231 : 0001-07-01 00:00:00     200    10512       0 :      30.000      30.000      30.000 : -2            
   232 : 0001-07-01 00:00:00     150    10512       0 :      30.000      30.000      30.000 : -2            
   233 : 0001-07-01 00:00:00     100    10512       0 :      30.000      30.000      30.000 : -2            
   234 : 0001-07-01 00:00:00      70    10512       0 :      30.000      30.000      30.000 : -2            
   235 : 0001-07-01 00:00:00      50    10512       0 :      30.000      30.000      30.000 : -2            
   236 : 0001-07-01 00:00:00      30    10512       0 :      30.000      30.000      30.000 : -2            
   237 : 0001-07-01 00:00:00      20    10512       0 :      30.000      30.000      30.000 : -2            
   238 : 0001-07-01 00:00:00      10    10512       0 :      30.000      30.000      30.000 : -2            
   239 : 0001-08-01 00:00:00    1000    10512       0 :      240.24      283.50      313.86 : -1            
   240 : 0001-08-01 00:00:00     925    10512       0 :      236.84      279.72      309.74 : -1            
   241 : 0001-08-01 00:00:00     850    10512       0 :      233.34      276.40      304.65 : -1            
   242 : 0001-08-01 00:00:00     700    10512       0 :      224.03      268.69      291.25 : -1            
   243 : 0001-08-01 00:00:00     600    10512       0 :      220.36      262.56      282.88 : -1            
   244 : 0001-08-01 00:00:00     500    10512       0 :      225.99      254.29      273.60 : -1            
   245 : 0001-08-01 00:00:00     400    10512       0 :      218.25      243.66      261.67 : -1            
   246 : 0001-08-01 00:00:00     300    10512       0 :      207.01      230.33      248.48 : -1            
   247 : 0001-08-01 00:00:00     250    10512       0 :      202.09      223.33      238.82 : -1            
   248 : 0001-08-01 00:00:00     200    10512       0 :      197.83      217.71      227.60 : -1            
   249 : 0001-08-01 00:00:00     150    10512       0 :      193.88      212.34      228.87 : -1            
   250 : 0001-08-01 00:00:00     100    10512       0 :      189.06      207.64      228.90 : -1            
   251 : 0001-08-01 00:00:00      70    10512       0 :      185.53      208.71      228.37 : -1            
   252 : 0001-08-01 00:00:00      50    10512       0 :      183.68      210.91      228.15 : -1            
   253 : 0001-08-01 00:00:00      30    10512       0 :      183.90      214.43      228.84 : -1            
   254 : 0001-08-01 00:00:00      20    10512       0 :      186.81      218.09      230.87 : -1            
   255 : 0001-08-01 00:00:00      10    10512       0 :      196.98      225.49      236.95 : -1            
   256 : 0001-08-01 00:00:00    1000    10512       0 :      30.000      30.000      30.000 : -2            
   257 : 0001-08-01 00:00:00     925    10512       0 :      30.000      30.000      30.000 : -2            
   258 : 0001-08-01 00:00:00     850    10512       0 :      30.000      30.000      30.000 : -2            
   259 : 0001-08-01 00:00:00     700    10512       0 :      30.000      30.000      30.000 : -2            
   260 : 0001-08-01 00:00:00     600    10512       0 :      30.000      30.000      30.000 : -2            
   261 : 0001-08-01 00:00:00     500    10512       0 :      30.000      30.000      30.000 : -2            
   262 : 0001-08-01 00:00:00     400    10512       0 :      30.000      30.000      30.000 : -2            
   263 : 0001-08-01 00:00:00     300    10512       0 :      30.000      30.000      30.000 : -2            
   264 : 0001-08-01 00:00:00     250    10512       0 :      30.000      30.000      30.000 : -2            
   265 : 0001-08-01 00:00:00     200    10512       0 :      30.000      30.000      30.000 : -2            
   266 : 0001-08-01 00:00:00     150    10512       0 :      30.000      30.000      30.000 : -2            
   267 : 0001-08-01 00:00:00     100    10512       0 :      30.000      30.000      30.000 : -2            
   268 : 0001-08-01 00:00:00      70    10512       0 :      30.000      30.000      30.000 : -2            
   269 : 0001-08-01 00:00:00      50    10512       0 :      30.000      30.000      30.000 : -2            
   270 : 0001-08-01 00:00:00      30    10512       0 :      30.000      30.000      30.000 : -2            
   271 : 0001-08-01 00:00:00      20    10512       0 :      30.000      30.000      30.000 : -2            
   272 : 0001-08-01 00:00:00      10    10512       0 :      30.000      30.000      30.000 : -2            
   273 : 0001-09-01 00:00:00    1000    10512       0 :      240.23      282.33      310.62 : -1            
   274 : 0001-09-01 00:00:00     925    10512       0 :      236.82      278.45      306.57 : -1            
   275 : 0001-09-01 00:00:00     850    10512       0 :      233.30      275.17      302.69 : -1            
   276 : 0001-09-01 00:00:00     700    10512       0 :      224.30      267.52      287.75 : -1            
   277 : 0001-09-01 00:00:00     600    10512       0 :      220.57      261.44      279.39 : -1            
   278 : 0001-09-01 00:00:00     500    10512       0 :      226.64      253.27      270.47 : -1            
   279 : 0001-09-01 00:00:00     400    10512       0 :      218.74      242.71      259.99 : -1            
   280 : 0001-09-01 00:00:00     300    10512       0 :      207.07      229.54      246.18 : -1            
   281 : 0001-09-01 00:00:00     250    10512       0 :      202.11      222.83      236.26 : -1            
   282 : 0001-09-01 00:00:00     200    10512       0 :      197.70      217.31      225.81 : -1            
   283 : 0001-09-01 00:00:00     150    10512       0 :      194.32      211.94      225.79 : -1            
   284 : 0001-09-01 00:00:00     100    10512       0 :      190.51      207.45      224.55 : -1            
   285 : 0001-09-01 00:00:00      70    10512       0 :      188.30      208.72      223.33 : -1            
   286 : 0001-09-01 00:00:00      50    10512       0 :      187.90      211.08      223.93 : -1            
   287 : 0001-09-01 00:00:00      30    10512       0 :      191.19      214.93      225.46 : -1            
   288 : 0001-09-01 00:00:00      20    10512       0 :      196.52      218.80      227.26 : -1            
   289 : 0001-09-01 00:00:00      10    10512       0 :      210.95      226.44      233.35 : -1            
   290 : 0001-09-01 00:00:00    1000    10512       0 :      30.000      30.000      30.000 : -2            
   291 : 0001-09-01 00:00:00     925    10512       0 :      30.000      30.000      30.000 : -2            
   292 : 0001-09-01 00:00:00     850    10512       0 :      30.000      30.000      30.000 : -2            
   293 : 0001-09-01 00:00:00     700    10512       0 :      30.000      30.000      30.000 : -2            
   294 : 0001-09-01 00:00:00     600    10512       0 :      30.000      30.000      30.000 : -2            
   295 : 0001-09-01 00:00:00     500    10512       0 :      30.000      30.000      30.000 : -2            
   296 : 0001-09-01 00:00:00     400    10512       0 :      30.000      30.000      30.000 : -2            
   297 : 0001-09-01 00:00:00     300    10512       0 :      30.000      30.000      30.000 : -2            
   298 : 0001-09-01 00:00:00     250    10512       0 :      30.000      30.000      30.000 : -2            
   299 : 0001-09-01 00:00:00     200    10512       0 :      30.000      30.000      30.000 : -2            
   300 : 0001-09-01 00:00:00     150    10512       0 :      30.000      30.000      30.000 : -2            
   301 : 0001-09-01 00:00:00     100    10512       0 :      30.000      30.000      30.000 : -2            
   302 : 0001-09-01 00:00:00      70    10512       0 :      30.000      30.000      30.000 : -2            
   303 : 0001-09-01 00:00:00      50    10512       0 :      30.000      30.000      30.000 : -2            
   304 : 0001-09-01 00:00:00      30    10512       0 :      30.000      30.000      30.000 : -2            
   305 : 0001-09-01 00:00:00      20    10512       0 :      30.000      30.000      30.000 : -2            
   306 : 0001-09-01 00:00:00      10    10512       0 :      30.000      30.000      30.000 : -2            
   307 : 0001-10-01 00:00:00    1000    10512       0 :      246.82      281.13      308.90 : -1            
   308 : 0001-10-01 00:00:00     925    10512       0 :      243.28      277.27      304.18 : -1            
   309 : 0001-10-01 00:00:00     850    10512       0 :      239.55      274.04      299.50 : -1            
   310 : 0001-10-01 00:00:00     700    10512       0 :      230.30      266.48      285.37 : -1            
   311 : 0001-10-01 00:00:00     600    10512       0 :      225.91      260.40      277.05 : -1            
   312 : 0001-10-01 00:00:00     500    10512       0 :      229.51      252.20      268.93 : -1            
   313 : 0001-10-01 00:00:00     400    10512       0 :      220.45      241.69      258.52 : -1            
   314 : 0001-10-01 00:00:00     300    10512       0 :      209.29      228.89      243.79 : -1            
   315 : 0001-10-01 00:00:00     250    10512       0 :      204.13      222.53      233.60 : -1            
   316 : 0001-10-01 00:00:00     200    10512       0 :      200.38      217.22      222.92 : -1            
   317 : 0001-10-01 00:00:00     150    10512       0 :      198.00      212.08      224.10 : -1            
   318 : 0001-10-01 00:00:00     100    10512       0 :      191.41      207.59      225.52 : -1            
   319 : 0001-10-01 00:00:00      70    10512       0 :      195.06      208.96      226.96 : -1            
   320 : 0001-10-01 00:00:00      50    10512       0 :      198.64      211.83      228.59 : -1            
   321 : 0001-10-01 00:00:00      30    10512       0 :      208.36      216.35      232.15 : -1            
   322 : 0001-10-01 00:00:00      20    10512       0 :      207.13      220.44      236.45 : -1            
   323 : 0001-10-01 00:00:00      10    10512       0 :      207.08      227.84      246.84 : -1            
   324 : 0001-10-01 00:00:00    1000    10512       0 :      30.000      30.000      30.000 : -2            
   325 : 0001-10-01 00:00:00     925    10512       0 :      30.000      30.000      30.000 : -2            
   326 : 0001-10-01 00:00:00     850    10512       0 :      30.000      30.000      30.000 : -2            
   327 : 0001-10-01 00:00:00     700    10512       0 :      30.000      30.000      30.000 : -2            
   328 : 0001-10-01 00:00:00     600    10512       0 :      30.000      30.000      30.000 : -2            
   329 : 0001-10-01 00:00:00     500    10512       0 :      30.000      30.000      30.000 : -2            
   330 : 0001-10-01 00:00:00     400    10512       0 :      30.000      30.000      30.000 : -2            
   331 : 0001-10-01 00:00:00     300    10512       0 :      30.000      30.000      30.000 : -2            
   332 : 0001-10-01 00:00:00     250    10512       0 :      30.000      30.000      30.000 : -2            
   333 : 0001-10-01 00:00:00     200    10512       0 :      30.000      30.000      30.000 : -2            
   334 : 0001-10-01 00:00:00     150    10512       0 :      30.000      30.000      30.000 : -2            
   335 : 0001-10-01 00:00:00     100    10512       0 :      30.000      30.000      30.000 : -2            
   336 : 0001-10-01 00:00:00      70    10512       0 :      30.000      30.000      30.000 : -2            
   337 : 0001-10-01 00:00:00      50    10512       0 :      30.000      30.000      30.000 : -2            
   338 : 0001-10-01 00:00:00      30    10512       0 :      30.000      30.000      30.000 : -2            
   339 : 0001-10-01 00:00:00      20    10512       0 :      30.000      30.000      30.000 : -2            
   340 : 0001-10-01 00:00:00      10    10512       0 :      30.000      30.000      30.000 : -2            
   341 : 0001-11-01 00:00:00    1000    10512       0 :      251.23      280.37      308.29 : -1            
   342 : 0001-11-01 00:00:00     925    10512       0 :      250.66      276.68      303.47 : -1            
   343 : 0001-11-01 00:00:00     850    10512       0 :      249.73      273.67      298.59 : -1            
   344 : 0001-11-01 00:00:00     700    10512       0 :      240.29      266.31      284.87 : -1            
   345 : 0001-11-01 00:00:00     600    10512       0 :      235.78      260.07      277.49 : -1            
   346 : 0001-11-01 00:00:00     500    10512       0 :      232.92      251.66      268.54 : -1            
   347 : 0001-11-01 00:00:00     400    10512       0 :      223.01      241.15      258.44 : -1            
   348 : 0001-11-01 00:00:00     300    10512       0 :      213.41      228.72      243.67 : -1            
   349 : 0001-11-01 00:00:00     250    10512       0 :      209.50      222.66      233.39 : -1            
   350 : 0001-11-01 00:00:00     200    10512       0 :      207.61      217.62      223.90 : -1            
   351 : 0001-11-01 00:00:00     150    10512       0 :      205.28      212.87      225.04 : -1            
   352 : 0001-11-01 00:00:00     100    10512       0 :      190.57      208.52      226.50 : -1            
   353 : 0001-11-01 00:00:00      70    10512       0 :      196.40      209.84      228.58 : -1            
   354 : 0001-11-01 00:00:00      50    10512       0 :      203.16      213.05      231.17 : -1            
   355 : 0001-11-01 00:00:00      30    10512       0 :      199.32      217.58      236.23 : -1            
   356 : 0001-11-01 00:00:00      20    10512       0 :      197.87      221.33      240.90 : -1            
   357 : 0001-11-01 00:00:00      10    10512       0 :      198.35      228.07      251.74 : -1            
   358 : 0001-11-01 00:00:00    1000    10512       0 :      30.000      30.000      30.000 : -2            
   359 : 0001-11-01 00:00:00     925    10512       0 :      30.000      30.000      30.000 : -2            
   360 : 0001-11-01 00:00:00     850    10512       0 :      30.000      30.000      30.000 : -2            
   361 : 0001-11-01 00:00:00     700    10512       0 :      30.000      30.000      30.000 : -2            
   362 : 0001-11-01 00:00:00     600    10512       0 :      30.000      30.000      30.000 : -2            
   363 : 0001-11-01 00:00:00     500    10512       0 :      30.000      30.000      30.000 : -2            
   364 : 0001-11-01 00:00:00     400    10512       0 :      30.000      30.000      30.000 : -2            
   365 : 0001-11-01 00:00:00     300    10512       0 :      30.000      30.000      30.000 : -2            
   366 : 0001-11-01 00:00:00     250    10512       0 :      30.000      30.000      30.000 : -2            
   367 : 0001-11-01 00:00:00     200    10512       0 :      30.000      30.000      30.000 : -2            
   368 : 0001-11-01 00:00:00     150    10512       0 :      30.000      30.000      30.000 : -2            
   369 : 0001-11-01 00:00:00     100    10512       0 :      30.000      30.000      30.000 : -2            
   370 : 0001-11-01 00:00:00      70    10512       0 :      30.000      30.000      30.000 : -2            
   371 : 0001-11-01 00:00:00      50    10512       0 :      30.000      30.000      30.000 : -2            
   372 : 0001-11-01 00:00:00      30    10512       0 :      30.000      30.000      30.000 : -2            
   373 : 0001-11-01 00:00:00      20    10512       0 :      30.000      30.000      30.000 : -2            
   374 : 0001-11-01 00:00:00      10    10512       0 :      30.000      30.000      30.000 : -2            
   375 : 0001-12-01 00:00:00    1000    10512       0 :      244.64      280.02      307.61 : -1            
   376 : 0001-12-01 00:00:00     925    10512       0 :      244.45      276.45      302.78 : -1            
   377 : 0001-12-01 00:00:00     850    10512       0 :      247.16      273.67      298.01 : -1            
   378 : 0001-12-01 00:00:00     700    10512       0 :      245.93      266.47      284.99 : -1            
   379 : 0001-12-01 00:00:00     600    10512       0 :      240.76      260.09      277.85 : -1            
   380 : 0001-12-01 00:00:00     500    10512       0 :      233.10      251.59      268.87 : -1            
   381 : 0001-12-01 00:00:00     400    10512       0 :      223.03      241.12      258.66 : -1            
   382 : 0001-12-01 00:00:00     300    10512       0 :      213.34      229.08      244.10 : -1            
   383 : 0001-12-01 00:00:00     250    10512       0 :      211.47      223.37      233.99 : -1            
   384 : 0001-12-01 00:00:00     200    10512       0 :      210.82      218.65      224.96 : -1            
   385 : 0001-12-01 00:00:00     150    10512       0 :      205.32      214.25      226.20 : -1            
   386 : 0001-12-01 00:00:00     100    10512       0 :      189.47      209.78      228.99 : -1            
   387 : 0001-12-01 00:00:00      70    10512       0 :      194.24      210.60      232.76 : -1            
   388 : 0001-12-01 00:00:00      50    10512       0 :      198.15      213.67      236.05 : -1            
   389 : 0001-12-01 00:00:00      30    10512       0 :      195.21      218.01      240.52 : -1            
   390 : 0001-12-01 00:00:00      20    10512       0 :      194.79      221.70      243.70 : -1            
   391 : 0001-12-01 00:00:00      10    10512       0 :      197.78      228.74      251.76 : -1            
   392 : 0001-12-01 00:00:00    1000    10512       0 :      30.000      30.000      30.000 : -2            
   393 : 0001-12-01 00:00:00     925    10512       0 :      30.000      30.000      30.000 : -2            
   394 : 0001-12-01 00:00:00     850    10512       0 :      30.000      30.000      30.000 : -2            
   395 : 0001-12-01 00:00:00     700    10512       0 :      30.000      30.000      30.000 : -2            
   396 : 0001-12-01 00:00:00     600    10512       0 :      30.000      30.000      30.000 : -2            
   397 : 0001-12-01 00:00:00     500    10512       0 :      30.000      30.000      30.000 : -2            
   398 : 0001-12-01 00:00:00     400    10512       0 :      30.000      30.000      30.000 : -2            
   399 : 0001-12-01 00:00:00     300    10512       0 :      30.000      30.000      30.000 : -2            
   400 : 0001-12-01 00:00:00     250    10512       0 :      30.000      30.000      30.000 : -2            
   401 : 0001-12-01 00:00:00     200    10512       0 :      30.000      30.000      30.000 : -2            
   402 : 0001-12-01 00:00:00     150    10512       0 :      30.000      30.000      30.000 : -2            
   403 : 0001-12-01 00:00:00     100    10512       0 :      30.000      30.000      30.000 : -2            
   404 : 0001-12-01 00:00:00      70    10512       0 :      30.000      30.000      30.000 : -2            
   405 : 0001-12-01 00:00:00      50    10512       0 :      30.000      30.000      30.000 : -2            
   406 : 0001-12-01 00:00:00      30    10512       0 :      30.000      30.000      30.000 : -2            
   407 : 0001-12-01 00:00:00      20    10512       0 :      30.000      30.000      30.000 : -2            
   408 : 0001-12-01 00:00:00      10    10512       0 :      30.000      30.000      30.000 : -2            
       :       Date     Time   Level Gridsize    Miss :     Minimum        Mean     Maximum : Parameter ID
cdo    info: Processed 4288896 values from 2 variables over 12 timesteps [0.28s 55MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo sinfon air.mon.ltm.nc 
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
   File format : NetCDF4 classic zip
    -1 : Institut Source   T Steptype Levels Num    Points Num Dtype : Parameter name
     1 : NCEP     NCEP/DOE v instant      17   1     10512   1  F32z : air           
     2 : NCEP     NCEP/DOE v instant      17   1     10512   1  I16  : valid_yr_count
   Grid coordinates :
     1 : lonlat                   : points=10512 (144x73)
                              lon : 0 to 357.5 by 2.5 degrees_east  circular
                              lat : 90 to -90 by -2.5 degrees_north
   Vertical coordinates :
     1 : pressure                 : levels=17
                            level : 1000 to 10 millibar
   Time coordinate :
                             time : 12 steps
     RefTime =  1800-01-01 00:00:00  Units = hours  Calendar = standard  Bounds = true
  YYYY-MM-DD hh:mm:ss  YYYY-MM-DD hh:mm:ss  YYYY-MM-DD hh:mm:ss  YYYY-MM-DD hh:mm:ss
  0001-01-01 00:00:00  0001-02-01 00:00:00  0001-03-01 00:00:00  0001-04-01 00:00:00
  0001-05-01 00:00:00  0001-06-01 00:00:00  0001-07-01 00:00:00  0001-08-01 00:00:00
  0001-09-01 00:00:00  0001-10-01 00:00:00  0001-11-01 00:00:00  0001-12-01 00:00:00
cdo    sinfon: Processed 2 variables over 12 timesteps [0.02s 46MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo pardes air.mon.ltm.nc 
Operator >pardes< not found!
Similar operators are:
pardup vardes 
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo griddes air.mon.ltm.nc 
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
#
# gridID 1
#
gridtype  = lonlat
gridsize  = 10512
datatype  = float
xsize     = 144
ysize     = 73
xname     = lon
xlongname = "Longitude"
xunits    = "degrees_east"
yname     = lat
ylongname = "Latitude"
yunits    = "degrees_north"
xfirst    = 0
xinc      = 2.5
yfirst    = 90
yinc      = -2.5
scanningMode = 64
cdo    griddes: Processed 2 variables [0.02s 46MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo ndate air.mon.ltm.nc 
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
12
cdo    ndate: Processed 2 variables over 12 timesteps [0.02s 46MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo nmon air.mon.ltm.nc 
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
12
cdo    nmon: Processed 2 variables over 12 timesteps [0.02s 46MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo ntime air.mon.ltm.nc 
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
12
cdo    ntime: Processed 2 variables [0.02s 46MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo showatts air.mon.ltm.nc 
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
air:
   standard_name = "air_temperature"
   long_name = "Long Term Mean Monthly Air Temperature on Pressure Levels"
   units = "degK"
   missing_value = -9.96921e+36
cdo    showatts (Warning): Unsupported type 216 name precision
cdo    showatts (Warning): Unsupported type 216 name least_significant_digit
cdo    showatts (Warning): Unsupported type 216 name GRIB_id
   GRIB_name = "TMP"
   var_desc = "Air temperature"
   dataset = "NCEP/DOE AMIP-II Reanalysis (Reanalysis-2) Monthly Averages"
   level_desc = "Pressure Levels"
   statistic = "Long Term Mean"
   parent_stat = "Individual Obs"
   cell_methods = "time: mean (monthly from 6-hourly values)"
   actual_range = 183.0121f, 314.302f
valid_yr_count:
   long_name = "count of non-missing values used in mean"
   missing_value = 32767
Global:
   Conventions = "CF-1.0"
   title = "Monthly NCEP/DOE Reanalysis 2"
   comments = "Data is from \n"
             "NCEP/DOE AMIP-II Reanalysis (Reanalysis-2)\n"
             "(4x/day).  It consists of most variables interpolated to\n"
             "pressure surfaces from model (sigma) surfaces."
   platform = "Model"
   dataset_title = "NCEP-DOE AMIP-II Reanalysis"
   References = "https://www.psl.noaa.gov/data/gridded/data.ncep.reanalysis2.html"
   source_url = "http://www.cpc.ncep.noaa.gov/products/wesley/reanalysis2/"
   history = "Created 2022/01/11 by doMonthLTMNC4"
   not_missing_threshold_percent = "minimum 3% values input to have non-missing output value"
cdo    showatts: Processed 2 variables [0.00s 46MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo showlevel air.mon.ltm.nc 
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
 1000 925 850 700 600 500 400 300 250 200 150 100 70 50 30 20 10
 1000 925 850 700 600 500 400 300 250 200 150 100 70 50 30 20 10
cdo    showlevel: Processed 2 variables [0.02s 46MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo selname,air air.mon.ltm.nc only_air.nc
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
cdo    selname: Processed 2144448 values from 2 variables over 12 timesteps [0.22s 65MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo showatts only_air.nc 
air:
   standard_name = "air_temperature"
   long_name = "Long Term Mean Monthly Air Temperature on Pressure Levels"
   units = "degK"
   missing_value = -9.96921e+36
cdo    showatts (Warning): Unsupported type 216 name precision
cdo    showatts (Warning): Unsupported type 216 name least_significant_digit
cdo    showatts (Warning): Unsupported type 216 name GRIB_id
   GRIB_name = "TMP"
   var_desc = "Air temperature"
   dataset = "NCEP/DOE AMIP-II Reanalysis (Reanalysis-2) Monthly Averages"
   level_desc = "Pressure Levels"
   statistic = "Long Term Mean"
   parent_stat = "Individual Obs"
   cell_methods = "time: mean (monthly from 6-hourly values)"
   actual_range = 183.0121f, 314.302f
Global:
   Conventions = "CF-1.0"
   title = "Monthly NCEP/DOE Reanalysis 2"
   comments = "Data is from \n"
             "NCEP/DOE AMIP-II Reanalysis (Reanalysis-2)\n"
             "(4x/day).  It consists of most variables interpolated to\n"
             "pressure surfaces from model (sigma) surfaces."
   platform = "Model"
   dataset_title = "NCEP-DOE AMIP-II Reanalysis"
   References = "https://www.psl.noaa.gov/data/gridded/data.ncep.reanalysis2.html"
   source_url = "http://www.cpc.ncep.noaa.gov/products/wesley/reanalysis2/"
   history = "Mon Jan 30 17:41:29 2023: cdo selname,air air.mon.ltm.nc only_air.nc\n"
             "Created 2022/01/11 by doMonthLTMNC4"
   not_missing_threshold_percent = "minimum 3% values input to have non-missing output value"
cdo    showatts: Processed 1 variable [0.02s 46MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo info only_air.nc 
    -1 :       Date     Time   Level Gridsize    Miss :     Minimum        Mean     Maximum : Parameter ID
     1 : 0001-01-01 00:00:00    1000    10512       0 :      244.25      279.68      308.67 : -1            
     2 : 0001-01-01 00:00:00     925    10512       0 :      244.56      276.17      303.57 : -1            
     3 : 0001-01-01 00:00:00     850    10512       0 :      247.07      273.46      297.96 : -1            
     4 : 0001-01-01 00:00:00     700    10512       0 :      245.16      266.39      284.88 : -1            
     5 : 0001-01-01 00:00:00     600    10512       0 :      239.81      260.13      277.66 : -1            
     6 : 0001-01-01 00:00:00     500    10512       0 :      232.17      251.66      268.99 : -1            
     7 : 0001-01-01 00:00:00     400    10512       0 :      222.35      241.23      258.82 : -1            
     8 : 0001-01-01 00:00:00     300    10512       0 :      212.77      229.50      244.29 : -1            
     9 : 0001-01-01 00:00:00     250    10512       0 :      210.36      224.09      234.37 : -1            
    10 : 0001-01-01 00:00:00     200    10512       0 :      209.07      219.68      227.75 : -1            
    11 : 0001-01-01 00:00:00     150    10512       0 :      205.56      215.25      230.66 : -1            
    12 : 0001-01-01 00:00:00     100    10512       0 :      190.07      210.29      231.98 : -1            
    13 : 0001-01-01 00:00:00      70    10512       0 :      193.78      210.66      234.17 : -1            
    14 : 0001-01-01 00:00:00      50    10512       0 :      198.20      213.72      235.77 : -1            
    15 : 0001-01-01 00:00:00      30    10512       0 :      197.87      218.36      237.98 : -1            
    16 : 0001-01-01 00:00:00      20    10512       0 :      199.96      222.39      240.74 : -1            
    17 : 0001-01-01 00:00:00      10    10512       0 :      206.35      230.12      248.99 : -1            
    18 : 0001-02-01 00:00:00    1000    10512       0 :      244.26      279.23      307.21 : -1            
    19 : 0001-02-01 00:00:00     925    10512       0 :      245.69      275.71      302.47 : -1            
    20 : 0001-02-01 00:00:00     850    10512       0 :      247.06      272.90      297.53 : -1            
    21 : 0001-02-01 00:00:00     700    10512       0 :      238.00      265.87      284.74 : -1            
    22 : 0001-02-01 00:00:00     600    10512       0 :      234.44      259.89      277.59 : -1            
    23 : 0001-02-01 00:00:00     500    10512       0 :      231.96      251.60      269.10 : -1            
    24 : 0001-02-01 00:00:00     400    10512       0 :      222.17      241.25      258.89 : -1            
    25 : 0001-02-01 00:00:00     300    10512       0 :      213.52      229.69      244.37 : -1            
    26 : 0001-02-01 00:00:00     250    10512       0 :      211.31      224.45      234.46 : -1            
    27 : 0001-02-01 00:00:00     200    10512       0 :      210.80      220.17      228.23 : -1            
    28 : 0001-02-01 00:00:00     150    10512       0 :      205.53      215.66      231.02 : -1            
    29 : 0001-02-01 00:00:00     100    10512       0 :      190.48      210.48      230.08 : -1            
    30 : 0001-02-01 00:00:00      70    10512       0 :      194.14      210.69      230.86 : -1            
    31 : 0001-02-01 00:00:00      50    10512       0 :      202.41      213.64      231.48 : -1            
    32 : 0001-02-01 00:00:00      30    10512       0 :      203.19      218.19      232.47 : -1            
    33 : 0001-02-01 00:00:00      20    10512       0 :      205.22      222.10      234.09 : -1            
    34 : 0001-02-01 00:00:00      10    10512       0 :      211.22      229.46      240.03 : -1            
    35 : 0001-03-01 00:00:00    1000    10512       0 :      245.45      279.24      307.91 : -1            
    36 : 0001-03-01 00:00:00     925    10512       0 :      242.03      275.66      303.62 : -1            
    37 : 0001-03-01 00:00:00     850    10512       0 :      238.15      272.66      298.63 : -1            
    38 : 0001-03-01 00:00:00     700    10512       0 :      229.38      265.47      285.29 : -1            
    39 : 0001-03-01 00:00:00     600    10512       0 :      225.98      259.59      277.35 : -1            
    40 : 0001-03-01 00:00:00     500    10512       0 :      231.29      251.42      268.96 : -1            
    41 : 0001-03-01 00:00:00     400    10512       0 :      223.39      241.11      258.75 : -1            
    42 : 0001-03-01 00:00:00     300    10512       0 :      214.90      229.49      244.08 : -1            
    43 : 0001-03-01 00:00:00     250    10512       0 :      212.87      224.13      233.91 : -1            
    44 : 0001-03-01 00:00:00     200    10512       0 :      212.65      219.82      226.07 : -1            
    45 : 0001-03-01 00:00:00     150    10512       0 :      205.87      215.38      227.49 : -1            
    46 : 0001-03-01 00:00:00     100    10512       0 :      191.14      210.26      225.75 : -1            
    47 : 0001-03-01 00:00:00      70    10512       0 :      195.22      210.41      224.80 : -1            
    48 : 0001-03-01 00:00:00      50    10512       0 :      203.62      213.14      224.12 : -1            
    49 : 0001-03-01 00:00:00      30    10512       0 :      210.09      217.34      224.83 : -1            
    50 : 0001-03-01 00:00:00      20    10512       0 :      211.82      220.94      226.34 : -1            
    51 : 0001-03-01 00:00:00      10    10512       0 :      215.93      227.64      232.44 : -1            
    52 : 0001-04-01 00:00:00    1000    10512       0 :      241.49      280.40      309.19 : -1            
    53 : 0001-04-01 00:00:00     925    10512       0 :      238.14      276.70      305.33 : -1            
    54 : 0001-04-01 00:00:00     850    10512       0 :      234.64      273.52      299.70 : -1            
    55 : 0001-04-01 00:00:00     700    10512       0 :      225.72      266.01      285.90 : -1            
    56 : 0001-04-01 00:00:00     600    10512       0 :      222.96      260.06      277.31 : -1            
    57 : 0001-04-01 00:00:00     500    10512       0 :      229.32      251.86      268.93 : -1            
    58 : 0001-04-01 00:00:00     400    10512       0 :      222.42      241.43      258.60 : -1            
    59 : 0001-04-01 00:00:00     300    10512       0 :      214.74      229.44      243.91 : -1            
    60 : 0001-04-01 00:00:00     250    10512       0 :      214.08      223.84      233.66 : -1            
    61 : 0001-04-01 00:00:00     200    10512       0 :      212.96      219.39      224.52 : -1            
    62 : 0001-04-01 00:00:00     150    10512       0 :      206.28      215.08      224.44 : -1            
    63 : 0001-04-01 00:00:00     100    10512       0 :      191.45      210.15      223.67 : -1            
    64 : 0001-04-01 00:00:00      70    10512       0 :      195.35      210.24      223.38 : -1            
    65 : 0001-04-01 00:00:00      50    10512       0 :      204.34      212.76      223.36 : -1            
    66 : 0001-04-01 00:00:00      30    10512       0 :      206.10      216.61      224.47 : -1            
    67 : 0001-04-01 00:00:00      20    10512       0 :      206.05      219.96      226.59 : -1            
    68 : 0001-04-01 00:00:00      10    10512       0 :      207.68      226.24      233.08 : -1            
    69 : 0001-05-01 00:00:00    1000    10512       0 :      239.99      281.99      311.40 : -1            
    70 : 0001-05-01 00:00:00     925    10512       0 :      236.62      278.16      306.77 : -1            
    71 : 0001-05-01 00:00:00     850    10512       0 :      233.20      274.87      301.29 : -1            
    72 : 0001-05-01 00:00:00     700    10512       0 :      224.00      267.19      287.01 : -1            
    73 : 0001-05-01 00:00:00     600    10512       0 :      221.88      261.13      277.27 : -1            
    74 : 0001-05-01 00:00:00     500    10512       0 :      228.08      252.81      269.40 : -1            
    75 : 0001-05-01 00:00:00     400    10512       0 :      220.59      242.24      259.14 : -1            
    76 : 0001-05-01 00:00:00     300    10512       0 :      211.54      229.81      244.94 : -1            
    77 : 0001-05-01 00:00:00     250    10512       0 :      208.86      223.85      235.05 : -1            
    78 : 0001-05-01 00:00:00     200    10512       0 :      208.72      219.05      228.38 : -1            
    79 : 0001-05-01 00:00:00     150    10512       0 :      206.25      214.57      227.92 : -1            
    80 : 0001-05-01 00:00:00     100    10512       0 :      191.85      209.68      228.06 : -1            
    81 : 0001-05-01 00:00:00      70    10512       0 :      195.37      209.72      228.01 : -1            
    82 : 0001-05-01 00:00:00      50    10512       0 :      195.64      212.10      228.40 : -1            
    83 : 0001-05-01 00:00:00      30    10512       0 :      193.36      215.65      229.26 : -1            
    84 : 0001-05-01 00:00:00      20    10512       0 :      193.91      218.91      231.10 : -1            
    85 : 0001-05-01 00:00:00      10    10512       0 :      198.03      225.16      236.81 : -1            
    86 : 0001-06-01 00:00:00    1000    10512       0 :      240.19      283.39      313.26 : -1            
    87 : 0001-06-01 00:00:00     925    10512       0 :      236.78      279.60      308.96 : -1            
    88 : 0001-06-01 00:00:00     850    10512       0 :      233.41      276.26      303.97 : -1            
    89 : 0001-06-01 00:00:00     700    10512       0 :      223.97      268.52      290.30 : -1            
    90 : 0001-06-01 00:00:00     600    10512       0 :      222.22      262.35      280.77 : -1            
    91 : 0001-06-01 00:00:00     500    10512       0 :      227.23      253.97      271.50 : -1            
    92 : 0001-06-01 00:00:00     400    10512       0 :      219.42      243.34      260.88 : -1            
    93 : 0001-06-01 00:00:00     300    10512       0 :      209.43      230.40      247.57 : -1            
    94 : 0001-06-01 00:00:00     250    10512       0 :      205.47      223.89      238.05 : -1            
    95 : 0001-06-01 00:00:00     200    10512       0 :      203.30      218.67      229.70 : -1            
    96 : 0001-06-01 00:00:00     150    10512       0 :      201.07      213.80      230.02 : -1            
    97 : 0001-06-01 00:00:00     100    10512       0 :      192.43      208.85      230.24 : -1            
    98 : 0001-06-01 00:00:00      70    10512       0 :      191.17      209.16      230.14 : -1            
    99 : 0001-06-01 00:00:00      50    10512       0 :      187.86      211.44      230.76 : -1            
   100 : 0001-06-01 00:00:00      30    10512       0 :      185.93      214.84      232.26 : -1            
   101 : 0001-06-01 00:00:00      20    10512       0 :      186.98      218.16      235.11 : -1            
   102 : 0001-06-01 00:00:00      10    10512       0 :      193.04      224.64      242.80 : -1            
   103 : 0001-07-01 00:00:00    1000    10512       0 :      240.43      283.86      314.30 : -1            
   104 : 0001-07-01 00:00:00     925    10512       0 :      237.25      280.18      310.15 : -1            
   105 : 0001-07-01 00:00:00     850    10512       0 :      233.87      276.84      305.06 : -1            
   106 : 0001-07-01 00:00:00     700    10512       0 :      224.18      269.12      291.82 : -1            
   107 : 0001-07-01 00:00:00     600    10512       0 :      220.65      262.95      283.44 : -1            
   108 : 0001-07-01 00:00:00     500    10512       0 :      225.79      254.65      274.05 : -1            
   109 : 0001-07-01 00:00:00     400    10512       0 :      218.02      244.03      262.10 : -1            
   110 : 0001-07-01 00:00:00     300    10512       0 :      207.70      230.78      249.10 : -1            
   111 : 0001-07-01 00:00:00     250    10512       0 :      203.00      223.82      239.56 : -1            
   112 : 0001-07-01 00:00:00     200    10512       0 :      199.74      218.26      229.82 : -1            
   113 : 0001-07-01 00:00:00     150    10512       0 :      196.69      213.00      230.35 : -1            
   114 : 0001-07-01 00:00:00     100    10512       0 :      191.19      208.09      230.54 : -1            
   115 : 0001-07-01 00:00:00      70    10512       0 :      187.01      208.85      230.33 : -1            
   116 : 0001-07-01 00:00:00      50    10512       0 :      184.20      211.03      230.84 : -1            
   117 : 0001-07-01 00:00:00      30    10512       0 :      183.01      214.38      232.38 : -1            
   118 : 0001-07-01 00:00:00      20    10512       0 :      184.66      217.82      235.37 : -1            
   119 : 0001-07-01 00:00:00      10    10512       0 :      192.34      224.69      243.22 : -1            
   120 : 0001-08-01 00:00:00    1000    10512       0 :      240.24      283.50      313.86 : -1            
   121 : 0001-08-01 00:00:00     925    10512       0 :      236.84      279.72      309.74 : -1            
   122 : 0001-08-01 00:00:00     850    10512       0 :      233.34      276.40      304.65 : -1            
   123 : 0001-08-01 00:00:00     700    10512       0 :      224.03      268.69      291.25 : -1            
   124 : 0001-08-01 00:00:00     600    10512       0 :      220.36      262.56      282.88 : -1            
   125 : 0001-08-01 00:00:00     500    10512       0 :      225.99      254.29      273.60 : -1            
   126 : 0001-08-01 00:00:00     400    10512       0 :      218.25      243.66      261.67 : -1            
   127 : 0001-08-01 00:00:00     300    10512       0 :      207.01      230.33      248.48 : -1            
   128 : 0001-08-01 00:00:00     250    10512       0 :      202.09      223.33      238.82 : -1            
   129 : 0001-08-01 00:00:00     200    10512       0 :      197.83      217.71      227.60 : -1            
   130 : 0001-08-01 00:00:00     150    10512       0 :      193.88      212.34      228.87 : -1            
   131 : 0001-08-01 00:00:00     100    10512       0 :      189.06      207.64      228.90 : -1            
   132 : 0001-08-01 00:00:00      70    10512       0 :      185.53      208.71      228.37 : -1            
   133 : 0001-08-01 00:00:00      50    10512       0 :      183.68      210.91      228.15 : -1            
   134 : 0001-08-01 00:00:00      30    10512       0 :      183.90      214.43      228.84 : -1            
   135 : 0001-08-01 00:00:00      20    10512       0 :      186.81      218.09      230.87 : -1            
   136 : 0001-08-01 00:00:00      10    10512       0 :      196.98      225.49      236.95 : -1            
   137 : 0001-09-01 00:00:00    1000    10512       0 :      240.23      282.33      310.62 : -1            
   138 : 0001-09-01 00:00:00     925    10512       0 :      236.82      278.45      306.57 : -1            
   139 : 0001-09-01 00:00:00     850    10512       0 :      233.30      275.17      302.69 : -1            
   140 : 0001-09-01 00:00:00     700    10512       0 :      224.30      267.52      287.75 : -1            
   141 : 0001-09-01 00:00:00     600    10512       0 :      220.57      261.44      279.39 : -1            
   142 : 0001-09-01 00:00:00     500    10512       0 :      226.64      253.27      270.47 : -1            
   143 : 0001-09-01 00:00:00     400    10512       0 :      218.74      242.71      259.99 : -1            
   144 : 0001-09-01 00:00:00     300    10512       0 :      207.07      229.54      246.18 : -1            
   145 : 0001-09-01 00:00:00     250    10512       0 :      202.11      222.83      236.26 : -1            
   146 : 0001-09-01 00:00:00     200    10512       0 :      197.70      217.31      225.81 : -1            
   147 : 0001-09-01 00:00:00     150    10512       0 :      194.32      211.94      225.79 : -1            
   148 : 0001-09-01 00:00:00     100    10512       0 :      190.51      207.45      224.55 : -1            
   149 : 0001-09-01 00:00:00      70    10512       0 :      188.30      208.72      223.33 : -1            
   150 : 0001-09-01 00:00:00      50    10512       0 :      187.90      211.08      223.93 : -1            
   151 : 0001-09-01 00:00:00      30    10512       0 :      191.19      214.93      225.46 : -1            
   152 : 0001-09-01 00:00:00      20    10512       0 :      196.52      218.80      227.26 : -1            
   153 : 0001-09-01 00:00:00      10    10512       0 :      210.95      226.44      233.35 : -1            
   154 : 0001-10-01 00:00:00    1000    10512       0 :      246.82      281.13      308.90 : -1            
   155 : 0001-10-01 00:00:00     925    10512       0 :      243.28      277.27      304.18 : -1            
   156 : 0001-10-01 00:00:00     850    10512       0 :      239.55      274.04      299.50 : -1            
   157 : 0001-10-01 00:00:00     700    10512       0 :      230.30      266.48      285.37 : -1            
   158 : 0001-10-01 00:00:00     600    10512       0 :      225.91      260.40      277.05 : -1            
   159 : 0001-10-01 00:00:00     500    10512       0 :      229.51      252.20      268.93 : -1            
   160 : 0001-10-01 00:00:00     400    10512       0 :      220.45      241.69      258.52 : -1            
   161 : 0001-10-01 00:00:00     300    10512       0 :      209.29      228.89      243.79 : -1            
   162 : 0001-10-01 00:00:00     250    10512       0 :      204.13      222.53      233.60 : -1            
   163 : 0001-10-01 00:00:00     200    10512       0 :      200.38      217.22      222.92 : -1            
   164 : 0001-10-01 00:00:00     150    10512       0 :      198.00      212.08      224.10 : -1            
   165 : 0001-10-01 00:00:00     100    10512       0 :      191.41      207.59      225.52 : -1            
   166 : 0001-10-01 00:00:00      70    10512       0 :      195.06      208.96      226.96 : -1            
   167 : 0001-10-01 00:00:00      50    10512       0 :      198.64      211.83      228.59 : -1            
   168 : 0001-10-01 00:00:00      30    10512       0 :      208.36      216.35      232.15 : -1            
   169 : 0001-10-01 00:00:00      20    10512       0 :      207.13      220.44      236.45 : -1            
   170 : 0001-10-01 00:00:00      10    10512       0 :      207.08      227.84      246.84 : -1            
   171 : 0001-11-01 00:00:00    1000    10512       0 :      251.23      280.37      308.29 : -1            
   172 : 0001-11-01 00:00:00     925    10512       0 :      250.66      276.68      303.47 : -1            
   173 : 0001-11-01 00:00:00     850    10512       0 :      249.73      273.67      298.59 : -1            
   174 : 0001-11-01 00:00:00     700    10512       0 :      240.29      266.31      284.87 : -1            
   175 : 0001-11-01 00:00:00     600    10512       0 :      235.78      260.07      277.49 : -1            
   176 : 0001-11-01 00:00:00     500    10512       0 :      232.92      251.66      268.54 : -1            
   177 : 0001-11-01 00:00:00     400    10512       0 :      223.01      241.15      258.44 : -1            
   178 : 0001-11-01 00:00:00     300    10512       0 :      213.41      228.72      243.67 : -1            
   179 : 0001-11-01 00:00:00     250    10512       0 :      209.50      222.66      233.39 : -1            
   180 : 0001-11-01 00:00:00     200    10512       0 :      207.61      217.62      223.90 : -1            
   181 : 0001-11-01 00:00:00     150    10512       0 :      205.28      212.87      225.04 : -1            
   182 : 0001-11-01 00:00:00     100    10512       0 :      190.57      208.52      226.50 : -1            
   183 : 0001-11-01 00:00:00      70    10512       0 :      196.40      209.84      228.58 : -1            
   184 : 0001-11-01 00:00:00      50    10512       0 :      203.16      213.05      231.17 : -1            
   185 : 0001-11-01 00:00:00      30    10512       0 :      199.32      217.58      236.23 : -1            
   186 : 0001-11-01 00:00:00      20    10512       0 :      197.87      221.33      240.90 : -1            
   187 : 0001-11-01 00:00:00      10    10512       0 :      198.35      228.07      251.74 : -1            
   188 : 0001-12-01 00:00:00    1000    10512       0 :      244.64      280.02      307.61 : -1            
   189 : 0001-12-01 00:00:00     925    10512       0 :      244.45      276.45      302.78 : -1            
   190 : 0001-12-01 00:00:00     850    10512       0 :      247.16      273.67      298.01 : -1            
   191 : 0001-12-01 00:00:00     700    10512       0 :      245.93      266.47      284.99 : -1            
   192 : 0001-12-01 00:00:00     600    10512       0 :      240.76      260.09      277.85 : -1            
   193 : 0001-12-01 00:00:00     500    10512       0 :      233.10      251.59      268.87 : -1            
   194 : 0001-12-01 00:00:00     400    10512       0 :      223.03      241.12      258.66 : -1            
   195 : 0001-12-01 00:00:00     300    10512       0 :      213.34      229.08      244.10 : -1            
   196 : 0001-12-01 00:00:00     250    10512       0 :      211.47      223.37      233.99 : -1            
   197 : 0001-12-01 00:00:00     200    10512       0 :      210.82      218.65      224.96 : -1            
   198 : 0001-12-01 00:00:00     150    10512       0 :      205.32      214.25      226.20 : -1            
   199 : 0001-12-01 00:00:00     100    10512       0 :      189.47      209.78      228.99 : -1            
   200 : 0001-12-01 00:00:00      70    10512       0 :      194.24      210.60      232.76 : -1            
   201 : 0001-12-01 00:00:00      50    10512       0 :      198.15      213.67      236.05 : -1            
   202 : 0001-12-01 00:00:00      30    10512       0 :      195.21      218.01      240.52 : -1            
   203 : 0001-12-01 00:00:00      20    10512       0 :      194.79      221.70      243.70 : -1            
   204 : 0001-12-01 00:00:00      10    10512       0 :      197.78      228.74      251.76 : -1            
       :       Date     Time   Level Gridsize    Miss :     Minimum        Mean     Maximum : Parameter ID
cdo    info: Processed 2144448 values from 1 variable over 12 timesteps [0.03s 55MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo sinfon only_air.nc 
   File format : NetCDF4 classic
    -1 : Institut Source   T Steptype Levels Num    Points Num Dtype : Parameter name
     1 : NCEP     NCEP/DOE v instant      17   1     10512   1  F32  : air           
   Grid coordinates :
     1 : lonlat                   : points=10512 (144x73)
                              lon : 0 to 357.5 by 2.5 degrees_east  circular
                              lat : 90 to -90 by -2.5 degrees_north
   Vertical coordinates :
     1 : pressure                 : levels=17
                            level : 1000 to 10 millibar
   Time coordinate :
                             time : 12 steps
     RefTime =  1800-01-01 00:00:00  Units = hours  Calendar = standard  Bounds = true
  YYYY-MM-DD hh:mm:ss  YYYY-MM-DD hh:mm:ss  YYYY-MM-DD hh:mm:ss  YYYY-MM-DD hh:mm:ss
  0001-01-01 00:00:00  0001-02-01 00:00:00  0001-03-01 00:00:00  0001-04-01 00:00:00
  0001-05-01 00:00:00  0001-06-01 00:00:00  0001-07-01 00:00:00  0001-08-01 00:00:00
  0001-09-01 00:00:00  0001-10-01 00:00:00  0001-11-01 00:00:00  0001-12-01 00:00:00
cdo    sinfon: Processed 1 variable over 12 timesteps [0.02s 46MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo sellonlatbox,60,110,6,35 air.mon.ltm.nc india.nc
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
cdo    sellonlatbox: Processed 4288896 values from 2 variables over 12 timesteps [0.22s 57MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ncview india.nc 
Ncview 2.1.8 David W. Pierce  8 March 2017
http://meteora.ucsd.edu:80/~pierce/ncview_home_page.html
Copyright (C) 1993 through 2015, David W. Pierce
Ncview comes with ABSOLUTELY NO WARRANTY; for details type `ncview -w'.
This is free software licensed under the Gnu General Public License version 3; type `ncview -c' for redistribution details.

Warning: Cannot convert string "-*-lucida-bold-r-*-*-14-*-*-*-*-*-*-*" to type FontStruct
calculating min and maxes for air...
X connection to :0 broken (explicit kill or server shutdown).
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ncview india.nc 
Ncview 2.1.8 David W. Pierce  8 March 2017
http://meteora.ucsd.edu:80/~pierce/ncview_home_page.html
Copyright (C) 1993 through 2015, David W. Pierce
Ncview comes with ABSOLUTELY NO WARRANTY; for details type `ncview -w'.
This is free software licensed under the Gnu General Public License version 3; type `ncview -c' for redistribution details.

Warning: Cannot convert string "-*-lucida-bold-r-*-*-14-*-*-*-*-*-*-*" to type FontStruct
calculating min and maxes for air...
X connection to :0 broken (explicit kill or server shutdown).
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ls
air.mon.ltm.nc  india.nc  only_air.nc  session_1.ipynb
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo distgrid,2,3 air.mon.ltm.nc diff_grids.nc
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
cdo    distgrid: Processed 4288896 values from 2 variables over 12 timesteps [0.29s 76MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ls
air.mon.ltm.nc  diff_grids.nc00000.nc  diff_grids.nc00001.nc  diff_grids.nc00002.nc  diff_grids.nc00003.nc  diff_grids.nc00004.nc  diff_grids.nc00005.nc  india.nc  only_air.nc  session_1.ipynb
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo --version
Climate Data Operators version 2.0.4 (https://mpimet.mpg.de/cdo)
System: x86_64-pc-linux-gnu
CXX Compiler: g++ -std=gnu++14 -g -O2 -ffile-prefix-map=/build/cdo-hTyRvi/cdo-2.0.4=. -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -fopenmp -pthread
CXX version : g++ (Ubuntu 11.2.0-16ubuntu1) 11.2.0
C Compiler: gcc -g -O2 -ffile-prefix-map=/build/cdo-hTyRvi/cdo-2.0.4=. -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -Wall -pedantic -fPIC  -fopenmp -pthread -pthread
C version : gcc (Ubuntu 11.2.0-16ubuntu1) 11.2.0
F77 Compiler: f77 -g -O2 -ffile-prefix-map=/build/cdo-hTyRvi/cdo-2.0.4=. -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong
F77 version : GNU Fortran (Ubuntu 11.2.0-16ubuntu1) 11.2.0
Features: 39GB 12threads C++14 OpenMP45 Fortran PTHREADS HDF5 NC4/HDF5/threadsafe OPeNDAP SZ UDUNITS2 PROJ MAGICS CURL FFTW3 SSE2
Libraries: HDF5/1.10.7 proj/8.2.1 curl/7.81.0 magics/4.10.1
CDI data types: SizeType=size_t  DateType=int64_t
CDI file types: srv ext ieg grb1 grb2 nc1 nc2 nc4 nc4c nc5 
     CDI library version : 2.0.4
 ecCodes library version : 2.24.2
  NetCDF library version : 4.8.1 of Sep 29 2021 09:36:14 $
    hdf5 library version : library undefined
    exse library version : 1.4.2
    FILE library version : 1.9.1

shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo option -b 64
Operator >option< not found!
Similar operators are:
outputint 
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo -b 64

No operator given!

usage : cdo  [Options]  Operator1  [-Operator2  [-OperatorN]]

  Options:
    -a             Generate an absolute time axis
    -A             Dry run that shows processed cdo call
    --attribs      Lists all operators with choosen features or the attributes of given operator(s)
                   operator name or a combination of [arbitrary/filesOnly/onlyFirst/noOutput/obase]
    -b <nbits>     Set the number of bits for the output precision
                   (I8/I16/I32/F32/F64 for nc1/nc2/nc4/nc4c/nc5; U8/U16/U32 for nc4/nc4c/nc5; F32/F64 for grb2/srv/ext/ieg; P1 - P24 for grb1/grb2)
                   Add L or B to set the byteorder to Little or Big endian
    --cmor         CMOR conform NetCDF output
    -C, --color    Set behaviour of colorized output messages <auto,no,all>
    --double       Using double precision floats for data in memory.
    --eccodes      Use ecCodes to decode/encode GRIB1 messages
    --enableexcept <except>
                   Set individual floating-point traps (DIVBYZERO, INEXACT, INVALID, OVERFLOW, UNDERFLOW, ALL_EXCEPT)
    -f, --format <format>
                   Format of the output file. (grb1/grb2/nc1/nc2/nc4/nc4c/nc5/srv/ext/ieg)
    -g <grid>      Set default grid name or file. Available grids: 
                   F<XXX>, t<RES>, tl<RES>, global_<DXY>, r<NX>x<NY>, g<NX>x<NY>, gme<NI>, lon=<LON>/lat=<LAT>
    -h, --help     Help information for the operators
    --ignore_time_bounds  Ignores time bounds for time range statistics
    --no_history   Do not append to NetCDF "history" global attribute
    --netcdf_hdr_pad, --hdr_pad, --header_pad <nbr>
                   Pad NetCDF output header with nbr bytes
    -k <chunktype> NetCDF4 chunk type: auto, grid or lines
    -L             Lock IO (sequential access)
    -m <missval>   Set the missing value of non NetCDF files (default: -9e+33)
    -O             Overwrite existing output file, if checked
    --operators    List of all operators
    --pedantic     Warnings count as errors
    -P <nthreads>  Set number of OpenMP threads
    --percentile <method>
                   Percentile method: nrank, nist, rtype8, numpy, numpy_lower, numpy_higher, numpy_nearest
    --precision <float_digits[,double_digits]>
                   Precision to use in displaying floating-point data (default: 7,15)
    --reduce_dim   Reduce NetCDF dimensions
    --no_remap_weights Switch off generation of remap weights
    -R, --regular  Convert GRIB1 data from global reduced to regular Gaussian grid (cgribex only)
    -r             Generate a relative time axis
    -S             Create an extra output stream for the module TIMSTAT. This stream
                   contains the number of non missing values for each output period.
    -s, --silent   Silent mode
    --seed <seed>  Seed for a new sequence of pseudo-random numbers.
    --single       Using single precision floats for data in memory.
    --sortname     Alphanumeric sorting of NetCDF parameter names
    -t <codetab>   Set GRIB1 default parameter code table name or file (cgribex only)
                   Predefined tables:  echam4 echam5 echam6 mpiom1 ecmwf remo cosmo002 cosmo201 cosmo202 cosmo203 cosmo205 cosmo250
    --timestat_date <srcdate>
                   Target timestamp (temporal statistics): first, middle, midhigh or last source timestep.
    -V, --version  Print the version number
    -v, --verbose  Print extra details for some operators
    -w             Disable warning messages
    --worker <num> Number of worker to decode/decompress GRIB records
    -z szip        SZIP compression of GRIB1 records
       aec         AEC compression of GRIB2 records
       jpeg        JPEG compression of GRIB2 records
        zip[_1-9]  Deflate compression of NetCDF4 variables
    --Dkext <debLev>   Setting debugLevel for extensions
    --outputGribDataScanningMode <mode>   Setting grib scanning mode for data in output file <0, 64, 96>; Default is 64

  Operators:
    Use option --operators for a list of all operators.

  CDO version 2.0.4, Copyright (C) 2003-2022 MPI für Meteorologie
  This is free software and comes with ABSOLUTELY NO WARRANTY
  Report bugs to <https://mpimet.mpg.de/cdo>
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo -r -f nc copy air.mon.ltm.nc time_relative_axis.nc
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
cdo    copy: Processed 4288896 values from 2 variables over 12 timesteps [0.24s 55MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo parades air.mon.ltm.nc 
Operator >parades< not found!
Similar operators are:
gradsdes vardes 
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo vardes air.mon.ltm.nc 
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
  -1  air           Long Term Mean Monthly Air Temperature on Pressure Levels [degK]
  -2  valid_yr_count  count of non-missing values used in mean
cdo    codetab: Processed 2 variables [0.02s 46MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo -h 
usage : cdo  [Options]  Operator1  [-Operator2  [-OperatorN]]

  Options:
    -a             Generate an absolute time axis
    -A             Dry run that shows processed cdo call
    --attribs      Lists all operators with choosen features or the attributes of given operator(s)
                   operator name or a combination of [arbitrary/filesOnly/onlyFirst/noOutput/obase]
    -b <nbits>     Set the number of bits for the output precision
                   (I8/I16/I32/F32/F64 for nc1/nc2/nc4/nc4c/nc5; U8/U16/U32 for nc4/nc4c/nc5; F32/F64 for grb2/srv/ext/ieg; P1 - P24 for grb1/grb2)
                   Add L or B to set the byteorder to Little or Big endian
    --cmor         CMOR conform NetCDF output
    -C, --color    Set behaviour of colorized output messages <auto,no,all>
    --double       Using double precision floats for data in memory.
    --eccodes      Use ecCodes to decode/encode GRIB1 messages
    --enableexcept <except>
                   Set individual floating-point traps (DIVBYZERO, INEXACT, INVALID, OVERFLOW, UNDERFLOW, ALL_EXCEPT)
    -f, --format <format>
                   Format of the output file. (grb1/grb2/nc1/nc2/nc4/nc4c/nc5/srv/ext/ieg)
    -g <grid>      Set default grid name or file. Available grids: 
                   F<XXX>, t<RES>, tl<RES>, global_<DXY>, r<NX>x<NY>, g<NX>x<NY>, gme<NI>, lon=<LON>/lat=<LAT>
    -h, --help     Help information for the operators
    --ignore_time_bounds  Ignores time bounds for time range statistics
    --no_history   Do not append to NetCDF "history" global attribute
    --netcdf_hdr_pad, --hdr_pad, --header_pad <nbr>
                   Pad NetCDF output header with nbr bytes
    -k <chunktype> NetCDF4 chunk type: auto, grid or lines
    -L             Lock IO (sequential access)
    -m <missval>   Set the missing value of non NetCDF files (default: -9e+33)
    -O             Overwrite existing output file, if checked
    --operators    List of all operators
    --pedantic     Warnings count as errors
    -P <nthreads>  Set number of OpenMP threads
    --percentile <method>
                   Percentile method: nrank, nist, rtype8, numpy, numpy_lower, numpy_higher, numpy_nearest
    --precision <float_digits[,double_digits]>
                   Precision to use in displaying floating-point data (default: 7,15)
    --reduce_dim   Reduce NetCDF dimensions
    --no_remap_weights Switch off generation of remap weights
    -R, --regular  Convert GRIB1 data from global reduced to regular Gaussian grid (cgribex only)
    -r             Generate a relative time axis
    -S             Create an extra output stream for the module TIMSTAT. This stream
                   contains the number of non missing values for each output period.
    -s, --silent   Silent mode
    --seed <seed>  Seed for a new sequence of pseudo-random numbers.
    --single       Using single precision floats for data in memory.
    --sortname     Alphanumeric sorting of NetCDF parameter names
    -t <codetab>   Set GRIB1 default parameter code table name or file (cgribex only)
                   Predefined tables:  echam4 echam5 echam6 mpiom1 ecmwf remo cosmo002 cosmo201 cosmo202 cosmo203 cosmo205 cosmo250
    --timestat_date <srcdate>
                   Target timestamp (temporal statistics): first, middle, midhigh or last source timestep.
    -V, --version  Print the version number
    -v, --verbose  Print extra details for some operators
    -w             Disable warning messages
    --worker <num> Number of worker to decode/decompress GRIB records
    -z szip        SZIP compression of GRIB1 records
       aec         AEC compression of GRIB2 records
       jpeg        JPEG compression of GRIB2 records
        zip[_1-9]  Deflate compression of NetCDF4 variables
    --Dkext <debLev>   Setting debugLevel for extensions
    --outputGribDataScanningMode <mode>   Setting grib scanning mode for data in output file <0, 64, 96>; Default is 64

  Operators:
    Use option --operators for a list of all operators.

  CDO version 2.0.4, Copyright (C) 2003-2022 MPI für Meteorologie
  This is free software and comes with ABSOLUTELY NO WARRANTY
  Report bugs to <https://mpimet.mpg.de/cdo>
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ncview diff_grids.nc0000
Ncview 2.1.8 David W. Pierce  8 March 2017
http://meteora.ucsd.edu:80/~pierce/ncview_home_page.html
Copyright (C) 1993 through 2015, David W. Pierce
Ncview comes with ABSOLUTELY NO WARRANTY; for details type `ncview -w'.
This is free software licensed under the Gnu General Public License version 3; type `ncview -c' for redistribution details.

ncview: can't open file diff_grids.nc0000 : No such file or directory
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ncview india.nc 
Ncview 2.1.8 David W. Pierce  8 March 2017
http://meteora.ucsd.edu:80/~pierce/ncview_home_page.html
Copyright (C) 1993 through 2015, David W. Pierce
Ncview comes with ABSOLUTELY NO WARRANTY; for details type `ncview -w'.
This is free software licensed under the Gnu General Public License version 3; type `ncview -c' for redistribution details.

Warning: Cannot convert string "-*-lucida-bold-r-*-*-14-*-*-*-*-*-*-*" to type FontStruct
calculating min and maxes for air...
X connection to :0 broken (explicit kill or server shutdown).
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ls -lrt
total 43160
-rw-rw-r-- 1 shiv shiv  8924795 Jan 25 18:55 air.mon.ltm.nc
-rw-rw-r-- 1 shiv shiv    59975 Jan 25 19:44 session_1.ipynb
-rw-rw-r-- 1 shiv shiv  8631364 Jan 30 17:41 only_air.nc
-rw-rw-r-- 1 shiv shiv   378762 Jan 30 17:47 india.nc
-rw-rw-r-- 1 shiv shiv  2187390 Jan 30 17:52 diff_grids.nc00001.nc
-rw-rw-r-- 1 shiv shiv  2187390 Jan 30 17:52 diff_grids.nc00000.nc
-rw-rw-r-- 1 shiv shiv  2187390 Jan 30 17:52 diff_grids.nc00003.nc
-rw-rw-r-- 1 shiv shiv  2187390 Jan 30 17:52 diff_grids.nc00002.nc
-rw-rw-r-- 1 shiv shiv  2275518 Jan 30 17:52 diff_grids.nc00005.nc
-rw-rw-r-- 1 shiv shiv  2275518 Jan 30 17:52 diff_grids.nc00004.nc
-rw-rw-r-- 1 shiv shiv 12870912 Jan 30 18:01 time_relative_axis.nc
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ncview diff_grids.nc0000.nc
Ncview 2.1.8 David W. Pierce  8 March 2017
http://meteora.ucsd.edu:80/~pierce/ncview_home_page.html
Copyright (C) 1993 through 2015, David W. Pierce
Ncview comes with ABSOLUTELY NO WARRANTY; for details type `ncview -w'.
This is free software licensed under the Gnu General Public License version 3; type `ncview -c' for redistribution details.

ncview: can't open file diff_grids.nc0000.nc : No such file or directory
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cp diff_grids.nc0000.nc 1.nc
cp: cannot stat 'diff_grids.nc0000.nc': No such file or directory
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ mv diff_grids.nc0000.nc 1.nc
mv: cannot stat 'diff_grids.nc0000.nc': No such file or directory
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ===
air.mon.ltm.nc         diff_grids.nc00001.nc  diff_grids.nc00003.nc  diff_grids.nc00005.nc  only_air.nc            time_relative_axis.nc  
diff_grids.nc00000.nc  diff_grids.nc00002.nc  diff_grids.nc00004.nc  india.nc               session_1.ipynb        
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ===
air.mon.ltm.nc         diff_grids.nc00001.nc  diff_grids.nc00003.nc  diff_grids.nc00005.nc  only_air.nc            time_relative_axis.nc  
diff_grids.nc00000.nc  diff_grids.nc00002.nc  diff_grids.nc00004.nc  india.nc               session_1.ipynb        
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ===
air.mon.ltm.nc         diff_grids.nc00001.nc  diff_grids.nc00003.nc  diff_grids.nc00005.nc  only_air.nc            time_relative_axis.nc  
diff_grids.nc00000.nc  diff_grids.nc00002.nc  diff_grids.nc00004.nc  india.nc               session_1.ipynb        
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ===
air.mon.ltm.nc         diff_grids.nc00001.nc  diff_grids.nc00003.nc  diff_grids.nc00005.nc  only_air.nc            time_relative_axis.nc  
diff_grids.nc00000.nc  diff_grids.nc00002.nc  diff_grids.nc00004.nc  india.nc               session_1.ipynb        
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ===
air.mon.ltm.nc         diff_grids.nc00001.nc  diff_grids.nc00003.nc  diff_grids.nc00005.nc  only_air.nc            time_relative_axis.nc  
diff_grids.nc00000.nc  diff_grids.nc00002.nc  diff_grids.nc00004.nc  india.nc               session_1.ipynb        
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ls -lrt
total 43160
-rw-rw-r-- 1 shiv shiv  8924795 Jan 25 18:55 air.mon.ltm.nc
-rw-rw-r-- 1 shiv shiv    59975 Jan 25 19:44 session_1.ipynb
-rw-rw-r-- 1 shiv shiv  8631364 Jan 30 17:41 only_air.nc
-rw-rw-r-- 1 shiv shiv   378762 Jan 30 17:47 india.nc
-rw-rw-r-- 1 shiv shiv  2187390 Jan 30 17:52 diff_grids.nc00001.nc
-rw-rw-r-- 1 shiv shiv  2187390 Jan 30 17:52 diff_grids.nc00000.nc
-rw-rw-r-- 1 shiv shiv  2187390 Jan 30 17:52 diff_grids.nc00003.nc
-rw-rw-r-- 1 shiv shiv  2187390 Jan 30 17:52 diff_grids.nc00002.nc
-rw-rw-r-- 1 shiv shiv  2275518 Jan 30 17:52 diff_grids.nc00005.nc
-rw-rw-r-- 1 shiv shiv  2275518 Jan 30 17:52 diff_grids.nc00004.nc
-rw-rw-r-- 1 shiv shiv 12870912 Jan 30 18:01 time_relative_axis.nc
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ cdo -r -f nc distgrid,2,3 air.mon.ltm.nc 1
Warning (cdfScanVarAttr): NetCDF: Variable not found - time_bnds
cdo    distgrid: Processed 4288896 values from 2 variables over 12 timesteps [0.17s 56MB].
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ls -lrt
total 55760
-rw-rw-r-- 1 shiv shiv  8924795 Jan 25 18:55 air.mon.ltm.nc
-rw-rw-r-- 1 shiv shiv    59975 Jan 25 19:44 session_1.ipynb
-rw-rw-r-- 1 shiv shiv  8631364 Jan 30 17:41 only_air.nc
-rw-rw-r-- 1 shiv shiv   378762 Jan 30 17:47 india.nc
-rw-rw-r-- 1 shiv shiv  2187390 Jan 30 17:52 diff_grids.nc00001.nc
-rw-rw-r-- 1 shiv shiv  2187390 Jan 30 17:52 diff_grids.nc00000.nc
-rw-rw-r-- 1 shiv shiv  2187390 Jan 30 17:52 diff_grids.nc00003.nc
-rw-rw-r-- 1 shiv shiv  2187390 Jan 30 17:52 diff_grids.nc00002.nc
-rw-rw-r-- 1 shiv shiv  2275518 Jan 30 17:52 diff_grids.nc00005.nc
-rw-rw-r-- 1 shiv shiv  2275518 Jan 30 17:52 diff_grids.nc00004.nc
-rw-rw-r-- 1 shiv shiv 12870912 Jan 30 18:01 time_relative_axis.nc
-rw-rw-r-- 1 shiv shiv  2207320 Jan 30 18:14 100005.nc
-rw-rw-r-- 1 shiv shiv  2207320 Jan 30 18:14 100004.nc
-rw-rw-r-- 1 shiv shiv  2119184 Jan 30 18:14 100003.nc
-rw-rw-r-- 1 shiv shiv  2119184 Jan 30 18:14 100002.nc
-rw-rw-r-- 1 shiv shiv  2119184 Jan 30 18:14 100001.nc
-rw-rw-r-- 1 shiv shiv  2119184 Jan 30 18:14 100000.nc
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ ncview 100004.nc 
Ncview 2.1.8 David W. Pierce  8 March 2017
http://meteora.ucsd.edu:80/~pierce/ncview_home_page.html
Copyright (C) 1993 through 2015, David W. Pierce
Ncview comes with ABSOLUTELY NO WARRANTY; for details type `ncview -w'.
This is free software licensed under the Gnu General Public License version 3; type `ncview -c' for redistribution details.

Warning: Cannot convert string "-*-lucida-bold-r-*-*-14-*-*-*-*-*-*-*" to type FontStruct
calculating min and maxes for air...
X connection to :0 broken (explicit kill or server shutdown).
shiv@stormbreaker:~/Documents/GitHub/EES405/lab_session_01$ 


