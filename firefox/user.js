/***
*
* _____
*(_   _)( )                               _
*  | |  | |__   _ __   __     __    ___  (_)  ___     __     _     ___     __
*  | |  |  _ `\( '__)/'__`\ /'__`\/' _ `\| |/' _ `\ /'__`\ /'_`\ /' _ `\ /'__`\
*  | |  | | | || |  (  ___/(  ___/| ( ) || || ( ) |(  ___/( (_) )| ( ) |(  ___/
*  (_)  (_) (_)(_)  `\____)`\____)(_) (_)(_)(_) (_)`\____)`\___/'(_) (_)`\____)
*
* author: threenineone or aiclys
* link: https://github.com/Aiclys
* Threenineone's Firefox config
*
*/
 
 
user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);
user_pref("browser.cache.disk.enable", false);
user_pref("browser.cache.memory.enable", true);
user_pref("browser.cache.memory.capacity", 524288);
user_pref("browser.sessionstore.interval", 15000000);
user_pref("extensions.pocket.enabled", false);
user_pref("reader.parse-on-load.enabled", false);
user_pref("accessibility.force_disabled", 1);
user_pref("browser.helperApps.deleteTempFileOnExit", true);
user_pref("browser.uitour.enabled", false);


/*** STARTUP ***/
/* set startup page
 * 0=blank, 1=home, 2=last visited page, 3=resume previous session*/
user_pref("browser.startup.page", 1);
/* set HOME+NEWWINDOW page
 * about:home=Firefox Home, custom URL, about:blank*/
user_pref("browser.startup.homepage", "about:home");
/* disable sponsored content on Firefox Home (Activity Stream)
 * [SETTING] Home>Firefox Home Content ***/
user_pref("browser.newtabpage.activity-stream.showSponsored", false); // [FF58+] Pocket > Sponsored Stories
user_pref("browser.newtabpage.activity-stream.showSponsoredTopSites", false); // [FF83+] Sponsored shortcuts
/* clear default topsites
 * [NOTE] This does not block you from adding your own ***/
user_pref("browser.newtabpage.activity-stream.default.sites", "");



/** NETWORKING ***/
//DNS over HTTPS
//Protects web requests from an ISP
//Please pick a provider you trust.
//Disable if you use PiHole, but tools like pfBlocker work fine.
// Cloudflare (default in US & Canada).
//Quad 9: https://dns.quad9.net/dns-query
// user_pref("network.trr.uri", "https://mozilla.cloudflare-dns.com/dns-query");
// user_pref("network.trr.mode", 2);
// Leave IPv6 enabled
user_pref("network.dns.disableIPv6", false);





/*** DEBLOATED FOX ***/
/* disable recommendation pane in about:addons (uses Google Analytics) ***/
user_pref("extensions.getAddons.showPane", false); // [HIDDEN PREF]
/* recommendations in about:addons' Extensions and Themes panes [FF68+] ***/
user_pref("extensions.htmlaboutaddons.recommendations.enabled", false);
/* personalized Extension Recommendations in about:addons and AMO [FF65+]
 * https://support.mozilla.org/kb/personalized-extension-recommendations ***/
user_pref("browser.discovery.enabled", false);



/** TELEMETRY ***/
/* disable new data submission */
user_pref("datareporting.policy.dataSubmissionEnabled", false);
/* disable Health Reports */
user_pref("datareporting.healthreport.uploadEnabled", false);
/* 0332: disable telemetry */
user_pref("toolkit.telemetry.unified", false);
user_pref("toolkit.telemetry.enabled", false);
user_pref("toolkit.telemetry.server", "data:,");
user_pref("toolkit.telemetry.archive.enabled", false);
user_pref("toolkit.telemetry.newProfilePing.enabled", false);
user_pref("toolkit.telemetry.shutdownPingSender.enabled", false);
user_pref("toolkit.telemetry.updatePing.enabled", false);
user_pref("toolkit.telemetry.bhrPing.enabled", false);
user_pref("toolkit.telemetry.firstShutdownPing.enabled", false);
/* disable Telemetry Coverage */
user_pref("toolkit.telemetry.coverage.opt-out", true); // [HIDDEN PREF]
user_pref("toolkit.coverage.opt-out", true); // [FF64+] [HIDDEN PREF]
user_pref("toolkit.coverage.endpoint.base", "");
/* disable PingCentre telemetry (used in several System Add-ons) [FF57+] */
user_pref("browser.ping-centre.telemetry", false);
/* disable Firefox Home (Activity Stream) telemetry ***/
user_pref("browser.newtabpage.activity-stream.feeds.telemetry", false);
user_pref("browser.newtabpage.activity-stream.telemetry", false);
user_pref("toolkit.telemetry.reportingpolicy.firstRun", false);
user_pref("toolkit.telemetry.shutdownPingSender.enabledFirstsession", false);
user_pref("browser.vpn_promo.enabled", false);
/* disable twitter/reddit and facebook ads in toolbar */
user_pref("browser.urlbar.quicksuggest.enabled", false);
user_pref("browser.urlbar.suggest.topsites", false); // [FF78+]ser_pref();



/** RESIST FINGERPRINTING ***/
user_pref("privacy.resistFingerprinting", true);
user_pref("privacy.resistFingerprinting.block_mozAddonManager", true);
user_pref("privacy.resistFingerprinting.letterboxing", false);



/** MOZILLA SHENANIGANS ***/
// Disable Mozilla password manager
user_pref("identity.rememberSignons", false);
// Disable Pocket (its trash)
user_pref("extensions.pocket.enabled", false);
user_pref("identity.fxaccounts.enabled", false);
// Disable WebGL because its a security risk
user_pref("webgl.disabled", true);
// Disable safe browsing as it is Google spyware
user_pref("browser.safebrowsing.malware.enabled", false);
user_pref("browser.safebrowsing.phishing.enabled", false);
user_pref("browser.safebrowsing.downloads.enabled", false);
// Reenable search engines
user_pref("keyword.enabled", true);
// Enable Search Engine suggestion
user_pref("browser.search.suggest.enabled", false);
user_pref("browser.urlbar.suggest.searches", false);
// Disk caching, which might improve performance if enabled.
user_pref("browser.cache.disk.enable", false);
// Enable favicons, the icons in bookmarks
user_pref("browser.shell.shortcutFavicons", true);
//WebRTC settings, things like video calls
   // user_pref("media.peerconnection.enabled", false);
// Disable Media Plugins
   // user_pref("media.gmp-provider.enabled", false);
// Disable DRM, FCKDRM
   // user_pref("media.gmp-widevinecdm.enabled", false);
user_pref("media.eme.enabled", false);
//Autoplaying settings
//0=Allow all, 1=Block non-muted media (default), 5=Block all
   // user_pref("media.autoplay.default", 5);
//If some websites REALLY need autoplaying...
//0=sticky (default), 1=transient, 2=user
user_pref("media.autoplay.blocking_policy", 2);
//Use Disconnect's blocklist to block ads
user_pref("browser.contentblocking.category", "strict");
//Clear data on shutdown
user_pref("privacy.sanitize.sanitizeOnShutdown", true);
user_pref("privacy.clearOnShutdown.cache", true);     // [DEFAULT: true]
user_pref("privacy.clearOnShutdown.downloads", true); // [DEFAULT: true]
user_pref("privacy.clearOnShutdown.formdata", true);  // [DEFAULT: true]
user_pref("privacy.clearOnShutdown.history", false);   // [DEFAULT: true]
user_pref("privacy.clearOnShutdown.sessions", false);  // [DEFAULT: true]
user_pref("privacy.clearOnShutdown.offlineApps", false); // [DEFAULT: false]
user_pref("privacy.clearOnShutdown.cookies", false);
//Delete cookies on close, but see below to make exceptions
/* 2801: delete cookies and site data on exit
 //* 0=keep until they expire (default), 2=keep until you close Firefox
 * [NOTE] A "cookie" block permission also controls localStorage/sessionStorage, indexedDB,
 * sharedWorkers and serviceWorkers. serviceWorkers require an "Allow" permission
 * [SETTING] Privacy & Security>Cookies and Site Data>Delete cookies and site data when Firefox is closed
 * [SETTING] to add site exceptions: Ctrl+I>Permissions>Cookies>Allow
 * [SETTING] to manage site exceptions: Options>Privacy & Security>Permissions>Settings ***/
user_pref("network.cookie.lifetimePolicy", 2);
//Disabling disk cache is better, but try this if you like performance
   // user_pref("privacy.clearsitedata.cache.enabled", true);




/** STUDIES ***/
/* disable Studies ***/
user_pref("app.shield.optoutstudies.enabled", false);
/* disable Normandy/Shield [FF60+]
 * Shield is a telemetry system that can push and test "recipes" ***/
user_pref("app.normandy.enabled", false);
user_pref("app.normandy.api_url", "");



/** CRASH REPORTS ***/
/* disable Crash Reports ***/
user_pref("breakpad.reportURL", "");
user_pref("browser.tabs.crashReporting.sendReport", false);
/* enforce no submission of backlogged Crash Reports [FF58+]
 * [SETTING] Privacy & Security>Firefox Data Collection & Use>Allow Firefox to send backlogged crash reports  ***/
user_pref("browser.crashReports.unsubmittedCheck.autoSubmit2", false);



/** MISC ***/
/* 0360: disable Captive Portal detection
 * [1] https://www.eff.org/deeplinks/2017/08/how-captive-portals-interfere-wireless-security-and-privacy ***/
user_pref("captivedetect.canonicalURL", "");
user_pref("network.captive-portal-service.enabled", false);
/* disable Network Connectivity checks
 * [1] https://bugzilla.mozilla.org/1460537 ***/
user_pref("network.connectivity-service.enabled", false);



/*** LOCALIZATION ETC ***/
/* use Mozilla geolocation service instead of Google.*/
user_pref("geo.provider.network.url", "https://location.services.mozilla.com/v1/geolocate?key=%MOZILLA_API_KEY%");
/* disable using the OS's geolocation service ***/
user_pref("geo.provider.ms-windows-location", false); // [WINDOWS]
user_pref("geo.provider.use_corelocation", false); // [MAC]
user_pref("geo.provider.use_gpsd", false); // [LINUX]
user_pref("geo.provider.use_geoclue", false); // [FF102+] [LINUX]


// Integrated calculator at urlbar
user_pref("browser.urlbar.suggest.calculator", true);
