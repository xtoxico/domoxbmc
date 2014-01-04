import xbmc
import xbmcaddon
import xbmcgui
import os
import simplejson
import socket

__addon__ = xbmcaddon.Addon()
__cwd__ = __addon__.getAddonInfo('path')
__scriptname__ = __addon__.getAddonInfo('name')
__version__ = __addon__.getAddonInfo('version')
__icon__ = __addon__.getAddonInfo('icon')
__ID__ = __addon__.getAddonInfo('id')
__language__ = __addon__.getLocalizedString

global g_jumpBackSecs
g_jumpBackSecs = 0

def log(msg):
  xbmc.log("### [%s] - %s" % (__scriptname__,msg,),level=xbmc.LOGDEBUG )

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.send(content)
    s.shutdown(socket.SHUT_WR)    

def getSetting(setting):
  return __addon__.getSetting(setting).strip()

#log( "[%s] - Version: %s Started" % (__scriptname__,__version__))

class MyPlayer( xbmc.Player ):
  def __init__( self, *args, **kwargs ):
    xbmc.Player.__init__( self )
    #log('MyPlayer - init')
  
  def onPlayBackStarted( self ):
    netcat("192.168.1.200",1729,"set salon off")
  
  def onPlayBackPaused( self ):
    netcat("192.168.1.200",1729,"set salon on")
  
  def onPlayBackResumed( self ):
    netcat("192.168.1.200",1729,"set salon off")

  def onPlayBackStopped( self ):
    netcat("192.168.1.200",1729,"set salon on")    
  
  def onPlayBackEnded( self ):
    netcat("192.168.1.200",1729,"set salon on")   

player_monitor = MyPlayer()

while not xbmc.abortRequested:
      xbmc.sleep(100)
