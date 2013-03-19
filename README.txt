========================================
ZenPacks.community.zenTwillScriptComponent
========================================

Developed by
============
Joseph Anderson

Description:
===========
This ZenPack provides a "Web Transaction" component and allows for the execution of 
Twill-based scripts within Zenoss

Each "Web Transaction" component has a "script" property that contains the script contents, which should be pasted
into the "script" textarea field of the "details" pane for the component.


Components
==========
  Component and Datasource class properties are specified in the provided "Definition.py" file.
	A basic RRD Template is also provided that executes the transtest.py script (provided) and graphs the output.

Installation
============
Describe the install process if anything is needed before or after standard
ZenPack installation.

Requirements
============
    Zenoss Versions Supported: 3.x, 4.x
    External Dependencies: Twill (twill-sh)
    ZenPack Dependencies: ZenPacks.community.ConstructionKit
    Installation Notes: zopectl restart; zenhub restart after installation
    Configuration: None

History
=======
Change History:

1.0 initial release

2.0
    added Zenoss 4.X support
    new dependency on "ConstructionKit" ZenPack to simplify current/future development
    <https://github.com/j053ph4/ZenPacks.community.ConstructionKit>

Tested
======
This ZenPack was tested with versions 3.2.1, 4.2.3

Source
======
https://github.com/j053ph4/ZenPacks.community.zenTwillScriptComponent

Known issues
============
None  
