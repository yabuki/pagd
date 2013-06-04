# -*- coding: utf-8 -*-

# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2013 R Pratap Chakravarthy

from   os.path               import join, isfile, abspath
from   pluggdapps.plugin     import Singleton, implements
from   pluggdapps.interfaces import ICommand

from   pagd.interfaces       import ILayout
from   pagd.lib              import json2dict

class Gen( Singleton ):
    """Sub-command plugin to generates the site at the given deployment 
    directory."""
    implements( ICommand )

    cmd = 'gen'
    description = 'Generate a static site for the give layout and content'

    #---- ICommand API
    def subparser( self, parser, subparsers ):
        """:meth:`pluggdapps.interfaces.ICommand.subparser` interface method.
        """
        self.subparser = subparsers.add_parser( 
                                self.cmd, description=self.description )
        self.subparser.set_defaults( handler=self.handle )
        self.subparser.add_argument(
                '-c', '--config-path',
                dest='configfile', default='config.json',
                help='The configuration used to generate the site')
        self.subparser.add_argument(
                '-t', '--build-target', dest='buildtarget',
                default='.',
                help="Location of target site that contains generated html.")
        self.subparser.add_argument(
                '-r', '--regen', dest='regen',
                action='store_true', default=False,
                help='Regenerate all source files.')
        return parser

    def handle( self, args ):
        """:meth:`pluggdapps.interfaces.ICommand.handle` interface method."""
        configfile = join( args.sitepath, args.configfile )
        if isfile(configfile) :
            siteconfig = json2dict( join( args.sitepath, configfile ))
            layoutname = siteconfig['layout']
        else :
            layoutname = args.layout
        sett = { 'sitepath' : args.sitepath }
        layout = self.qp( ILayout, layoutname, settings=sett )
        buildtarget = abspath( join( args.sitepath, args.buildtarget ))
        self.pa.loginfo(
            "Generating site at [%s] with layout [%s] ..." %
            (args.sitepath, layoutname))
        layout.generate(buildtarget, regen=args.regen)
        self.pa.loginfo("... complete")
