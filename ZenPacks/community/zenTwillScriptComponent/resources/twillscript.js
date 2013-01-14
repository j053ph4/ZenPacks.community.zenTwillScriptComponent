/*
 * Based on the configuration in ../../configure.zcml this JavaScript will only
 * be loaded when the user is looking at an ExampleDevice in the web interface.
 */

(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.TwillScriptPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'TwillScript',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'status'},
                {name: 'name'},
                {name: 'twillComponent'},
                {name: 'twillScript'},
                {name: 'twillURL'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'twillComponent',
                dataIndex: 'twillComponent',
                header: _t('Component'),
                sortable: true,
                width: 150
            },{
                id: 'twillURL',
                dataIndex: 'twillURL',
                header: _t('URL'),
                sortable: true,
                width: 150
            },{
                id: 'twillScript',
                dataIndex: 'twillScript',
                header: _t('Script'),
                sortable: true,
                width: 150
            },{
                id: 'status',
                dataIndex: 'status',
                header: _t('Status'),
                width: 70
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                sortable: true,
                width: 65
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                sortable: true,
                width: 65
            }
			]
        });
        ZC.TwillScriptPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('TwillScriptPanel', ZC.TwillScriptPanel);
ZC.registerName('TwillScript', _t('Twill Script'), _t('Twill Scripts'));

})();

