[#--
Copyright (C) 2020 HERE Europe B.V.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

SPDX-License-Identifier: Apache-2.0
License-Filename: LICENSE
--]
[#--
The notice file generated by this template consists of the following sections:

* The licenses and associated copyrights for all projects and packages merged into a single list.

Archived license files and excluded projects and packages are ignored.
--]
[#-- Add the licenses of the projects. --]
[#if projects?has_content]
This project contains or depends on third-party software components pursuant to the following licenses:

----
[#assign isFirst = true]
[#--
Merge the licenses and copyrights of all projects and packages into a single list. The licenses are filtered using
LicenseView.CONCLUDED_OR_REST. This is the default view which ignores declared and detected licenses if a license
conclusion for a package was made. For projects this is the same as LicenseView.ALL, because projects cannot have
concluded licenses. If copyrights were detected for a concluded license those statements are kept. Also filter all
licenses that are configured not to be included in notice files.
--]
[#assign mergedLicenses = helper.filterIncludeInNoticeFile(helper.mergeLicenses(projects + packages, helper.licenseView("CONCLUDED_OR_REST")))]
[#list mergedLicenses as resolvedLicense]
[#assign licenseText = licenseTextProvider.getLicenseText(resolvedLicense.license.simpleLicense())!""]
[#if licenseText?has_content]
[#if isFirst]
[#assign isFirst = false]
[#else]
----
[/#if]
[#assign copyrights = resolvedLicense.getCopyrights()]
[#list copyrights as copyright]
[#if copyright?is_first]

[/#if]
${copyright}
[/#list]

${licenseText}
[#assign exceptionText = licenseTextProvider.getLicenseText(resolvedLicense.license.exception()!"")!""]
[#if exceptionText?has_content]
${exceptionText}
[/#if]
[/#if]
[/#list]
[/#if]
