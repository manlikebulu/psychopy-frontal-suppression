#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.3),
    on June 19, 2026, at 11:56
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.1.3'
expName = 'stroop_oddball'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'Age': '',
    'Sex': ['Male','Female','Prefer not to say'],
    'Vision': ['Normal','Corrected'],
    'Handedness': ['Right','Left','Ambidexterous'],
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\TSC\\OneDrive\\Desktop\\stroop_oddball\\stroop_oddball_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Baseline_routine" ---
    baseline_screen = visual.TextStim(win=win, name='baseline_screen',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "stroop_Instruction" ---
    instructionStroop = visual.TextStim(win=win, name='instructionStroop',
        text='You are about to start a Stroop task. This task will last 6 minutes.\n\nIn each trial, a word will appear in a colored ink. Your task is to respond to the colour of the ink, not the meaning of the word.\n\nUse the following keys:\nR = Red, Y = Yellow, G = Green and B = Blue\n\nRemember:\n\nRespond to the COLOUR , not the word\nStay fast and accurate\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "stroop_trial" ---
    stroop_stim = visual.TextStim(win=win, name='stroop_stim',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_stroop = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "ITI" ---
    text = visual.TextStim(win=win, name='text',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "oddball_instruction" ---
    instructionOddball = visual.TextStim(win=win, name='instructionOddball',
        text='WELCOME\n\nIn this task, you will see a series of circles appear one at a time.\n\nMost of the circles will be BLACK, while a few will be RED.\n\nYOUR TASK:\n- Press the SPACEBAR as quickly and accurately as possible ONLY when you see a RED circle.\n- Do NOT press any key when you see a BLACK circle.\n\nRespond as fast as you can while staying accurate.\n\nFocus on the screen at all times, as the circles will appear quickly and in random order.\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "oddball_trial" ---
    circle_stim = visual.ShapeStim(
        win=win, name='circle_stim',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    key_resp_oddball = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "ITI" ---
    text = visual.TextStim(win=win, name='text',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Baseline_routine" ---
    # create an object to store info about Routine Baseline_routine
    Baseline_routine = data.Routine(
        name='Baseline_routine',
        components=[baseline_screen],
    )
    Baseline_routine.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for Baseline_routine
    Baseline_routine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Baseline_routine.tStart = globalClock.getTime(format='float')
    Baseline_routine.status = STARTED
    thisExp.addData('Baseline_routine.started', Baseline_routine.tStart)
    Baseline_routine.maxDuration = None
    # keep track of which components have finished
    Baseline_routineComponents = Baseline_routine.components
    for thisComponent in Baseline_routine.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Baseline_routine" ---
    thisExp.currentRoutine = Baseline_routine
    Baseline_routine.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 60.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *baseline_screen* updates
        
        # if baseline_screen is starting this frame...
        if baseline_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            baseline_screen.frameNStart = frameN  # exact frame index
            baseline_screen.tStart = t  # local t and not account for scr refresh
            baseline_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_screen, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'baseline_screen.started')
            # update status
            baseline_screen.status = STARTED
            baseline_screen.setAutoDraw(True)
        
        # if baseline_screen is active this frame...
        if baseline_screen.status == STARTED:
            # update params
            pass
        
        # if baseline_screen is stopping this frame...
        if baseline_screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > baseline_screen.tStartRefresh + 60.0-frameTolerance:
                # keep track of stop time/frame for later
                baseline_screen.tStop = t  # not accounting for scr refresh
                baseline_screen.tStopRefresh = tThisFlipGlobal  # on global time
                baseline_screen.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'baseline_screen.stopped')
                # update status
                baseline_screen.status = FINISHED
                baseline_screen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Baseline_routine,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            Baseline_routine.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if Baseline_routine.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in Baseline_routine.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Baseline_routine" ---
    for thisComponent in Baseline_routine.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Baseline_routine
    Baseline_routine.tStop = globalClock.getTime(format='float')
    Baseline_routine.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Baseline_routine.stopped', Baseline_routine.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Baseline_routine.maxDurationReached:
        routineTimer.addTime(-Baseline_routine.maxDuration)
    elif Baseline_routine.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-60.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "stroop_Instruction" ---
    # create an object to store info about Routine stroop_Instruction
    stroop_Instruction = data.Routine(
        name='stroop_Instruction',
        components=[instructionStroop],
    )
    stroop_Instruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for stroop_Instruction
    stroop_Instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    stroop_Instruction.tStart = globalClock.getTime(format='float')
    stroop_Instruction.status = STARTED
    thisExp.addData('stroop_Instruction.started', stroop_Instruction.tStart)
    stroop_Instruction.maxDuration = None
    # keep track of which components have finished
    stroop_InstructionComponents = stroop_Instruction.components
    for thisComponent in stroop_Instruction.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "stroop_Instruction" ---
    thisExp.currentRoutine = stroop_Instruction
    stroop_Instruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionStroop* updates
        
        # if instructionStroop is starting this frame...
        if instructionStroop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionStroop.frameNStart = frameN  # exact frame index
            instructionStroop.tStart = t  # local t and not account for scr refresh
            instructionStroop.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionStroop, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructionStroop.started')
            # update status
            instructionStroop.status = STARTED
            instructionStroop.setAutoDraw(True)
        
        # if instructionStroop is active this frame...
        if instructionStroop.status == STARTED:
            # update params
            pass
        
        # if instructionStroop is stopping this frame...
        if instructionStroop.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instructionStroop.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                instructionStroop.tStop = t  # not accounting for scr refresh
                instructionStroop.tStopRefresh = tThisFlipGlobal  # on global time
                instructionStroop.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instructionStroop.stopped')
                # update status
                instructionStroop.status = FINISHED
                instructionStroop.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=stroop_Instruction,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            stroop_Instruction.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if stroop_Instruction.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in stroop_Instruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "stroop_Instruction" ---
    for thisComponent in stroop_Instruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for stroop_Instruction
    stroop_Instruction.tStop = globalClock.getTime(format='float')
    stroop_Instruction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('stroop_Instruction.stopped', stroop_Instruction.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if stroop_Instruction.maxDurationReached:
        routineTimer.addTime(-stroop_Instruction.maxDuration)
    elif stroop_Instruction.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    stroop_loop = data.TrialHandler2(
        name='stroop_loop',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('stroop_conditions.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(stroop_loop)  # add the loop to the experiment
    thisStroop_loop = stroop_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStroop_loop.rgb)
    if thisStroop_loop != None:
        for paramName in thisStroop_loop:
            globals()[paramName] = thisStroop_loop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisStroop_loop in stroop_loop:
        stroop_loop.status = STARTED
        if hasattr(thisStroop_loop, 'status'):
            thisStroop_loop.status = STARTED
        currentLoop = stroop_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisStroop_loop.rgb)
        if thisStroop_loop != None:
            for paramName in thisStroop_loop:
                globals()[paramName] = thisStroop_loop[paramName]
        
        # --- Prepare to start Routine "stroop_trial" ---
        # create an object to store info about Routine stroop_trial
        stroop_trial = data.Routine(
            name='stroop_trial',
            components=[stroop_stim, key_resp_stroop],
        )
        stroop_trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        stroop_stim.setColor(color, colorSpace='rgb')
        stroop_stim.setText(word)
        # create starting attributes for key_resp_stroop
        key_resp_stroop.keys = []
        key_resp_stroop.rt = []
        _key_resp_stroop_allKeys = []
        # store start times for stroop_trial
        stroop_trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        stroop_trial.tStart = globalClock.getTime(format='float')
        stroop_trial.status = STARTED
        thisExp.addData('stroop_trial.started', stroop_trial.tStart)
        stroop_trial.maxDuration = None
        # keep track of which components have finished
        stroop_trialComponents = stroop_trial.components
        for thisComponent in stroop_trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "stroop_trial" ---
        thisExp.currentRoutine = stroop_trial
        stroop_trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # if trial has changed, end Routine now
            if hasattr(thisStroop_loop, 'status') and thisStroop_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stroop_stim* updates
            
            # if stroop_stim is starting this frame...
            if stroop_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stroop_stim.frameNStart = frameN  # exact frame index
                stroop_stim.tStart = t  # local t and not account for scr refresh
                stroop_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stroop_stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stroop_stim.started')
                # update status
                stroop_stim.status = STARTED
                stroop_stim.setAutoDraw(True)
            
            # if stroop_stim is active this frame...
            if stroop_stim.status == STARTED:
                # update params
                pass
            
            # if stroop_stim is stopping this frame...
            if stroop_stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stroop_stim.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    stroop_stim.tStop = t  # not accounting for scr refresh
                    stroop_stim.tStopRefresh = tThisFlipGlobal  # on global time
                    stroop_stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stroop_stim.stopped')
                    # update status
                    stroop_stim.status = FINISHED
                    stroop_stim.setAutoDraw(False)
            
            # *key_resp_stroop* updates
            waitOnFlip = False
            
            # if key_resp_stroop is starting this frame...
            if key_resp_stroop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_stroop.frameNStart = frameN  # exact frame index
                key_resp_stroop.tStart = t  # local t and not account for scr refresh
                key_resp_stroop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_stroop, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_stroop.started')
                # update status
                key_resp_stroop.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_stroop.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_stroop.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_stroop is stopping this frame...
            if key_resp_stroop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_stroop.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_stroop.tStop = t  # not accounting for scr refresh
                    key_resp_stroop.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp_stroop.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_stroop.stopped')
                    # update status
                    key_resp_stroop.status = FINISHED
                    key_resp_stroop.status = FINISHED
            if key_resp_stroop.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_stroop.getKeys(keyList=['r','b','y','g'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_stroop_allKeys.extend(theseKeys)
                if len(_key_resp_stroop_allKeys):
                    key_resp_stroop.keys = _key_resp_stroop_allKeys[-1].name  # just the last key pressed
                    key_resp_stroop.rt = _key_resp_stroop_allKeys[-1].rt
                    key_resp_stroop.duration = _key_resp_stroop_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_stroop.keys == str('')) or (key_resp_stroop.keys == ''):
                        key_resp_stroop.corr = 1
                    else:
                        key_resp_stroop.corr = 0
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=stroop_trial,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                stroop_trial.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if stroop_trial.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in stroop_trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stroop_trial" ---
        for thisComponent in stroop_trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for stroop_trial
        stroop_trial.tStop = globalClock.getTime(format='float')
        stroop_trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('stroop_trial.stopped', stroop_trial.tStop)
        # check responses
        if key_resp_stroop.keys in ['', [], None]:  # No response was made
            key_resp_stroop.keys = None
            # was no response the correct answer?!
            if str('').lower() == 'none':
               key_resp_stroop.corr = 1;  # correct non-response
            else:
               key_resp_stroop.corr = 0;  # failed to respond (incorrectly)
        # store data for stroop_loop (TrialHandler)
        stroop_loop.addData('key_resp_stroop.keys',key_resp_stroop.keys)
        stroop_loop.addData('key_resp_stroop.corr', key_resp_stroop.corr)
        if key_resp_stroop.keys != None:  # we had a response
            stroop_loop.addData('key_resp_stroop.rt', key_resp_stroop.rt)
            stroop_loop.addData('key_resp_stroop.duration', key_resp_stroop.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if stroop_trial.maxDurationReached:
            routineTimer.addTime(-stroop_trial.maxDuration)
        elif stroop_trial.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "ITI" ---
        # create an object to store info about Routine ITI
        ITI = data.Routine(
            name='ITI',
            components=[text],
        )
        ITI.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ITI
        ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ITI.tStart = globalClock.getTime(format='float')
        ITI.status = STARTED
        thisExp.addData('ITI.started', ITI.tStart)
        ITI.maxDuration = None
        # keep track of which components have finished
        ITIComponents = ITI.components
        for thisComponent in ITI.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ITI" ---
        thisExp.currentRoutine = ITI
        ITI.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisStroop_loop, 'status') and thisStroop_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=ITI,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                ITI.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if ITI.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in ITI.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ITI
        ITI.tStop = globalClock.getTime(format='float')
        ITI.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ITI.stopped', ITI.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ITI.maxDurationReached:
            routineTimer.addTime(-ITI.maxDuration)
        elif ITI.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisStroop_loop as finished
        if hasattr(thisStroop_loop, 'status'):
            thisStroop_loop.status = FINISHED
        # if awaiting a pause, pause now
        if stroop_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            stroop_loop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'stroop_loop'
    stroop_loop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "oddball_instruction" ---
    # create an object to store info about Routine oddball_instruction
    oddball_instruction = data.Routine(
        name='oddball_instruction',
        components=[instructionOddball],
    )
    oddball_instruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for oddball_instruction
    oddball_instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    oddball_instruction.tStart = globalClock.getTime(format='float')
    oddball_instruction.status = STARTED
    thisExp.addData('oddball_instruction.started', oddball_instruction.tStart)
    oddball_instruction.maxDuration = None
    # keep track of which components have finished
    oddball_instructionComponents = oddball_instruction.components
    for thisComponent in oddball_instruction.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "oddball_instruction" ---
    thisExp.currentRoutine = oddball_instruction
    oddball_instruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 60.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionOddball* updates
        
        # if instructionOddball is starting this frame...
        if instructionOddball.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionOddball.frameNStart = frameN  # exact frame index
            instructionOddball.tStart = t  # local t and not account for scr refresh
            instructionOddball.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionOddball, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructionOddball.started')
            # update status
            instructionOddball.status = STARTED
            instructionOddball.setAutoDraw(True)
        
        # if instructionOddball is active this frame...
        if instructionOddball.status == STARTED:
            # update params
            pass
        
        # if instructionOddball is stopping this frame...
        if instructionOddball.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instructionOddball.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                instructionOddball.tStop = t  # not accounting for scr refresh
                instructionOddball.tStopRefresh = tThisFlipGlobal  # on global time
                instructionOddball.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instructionOddball.stopped')
                # update status
                instructionOddball.status = FINISHED
                instructionOddball.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=oddball_instruction,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            oddball_instruction.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if oddball_instruction.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in oddball_instruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "oddball_instruction" ---
    for thisComponent in oddball_instruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for oddball_instruction
    oddball_instruction.tStop = globalClock.getTime(format='float')
    oddball_instruction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('oddball_instruction.stopped', oddball_instruction.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if oddball_instruction.maxDurationReached:
        routineTimer.addTime(-oddball_instruction.maxDuration)
    elif oddball_instruction.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-60.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    oddball_loop = data.TrialHandler2(
        name='oddball_loop',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('oddball_conditions.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(oddball_loop)  # add the loop to the experiment
    thisOddball_loop = oddball_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOddball_loop.rgb)
    if thisOddball_loop != None:
        for paramName in thisOddball_loop:
            globals()[paramName] = thisOddball_loop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisOddball_loop in oddball_loop:
        oddball_loop.status = STARTED
        if hasattr(thisOddball_loop, 'status'):
            thisOddball_loop.status = STARTED
        currentLoop = oddball_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisOddball_loop.rgb)
        if thisOddball_loop != None:
            for paramName in thisOddball_loop:
                globals()[paramName] = thisOddball_loop[paramName]
        
        # --- Prepare to start Routine "oddball_trial" ---
        # create an object to store info about Routine oddball_trial
        oddball_trial = data.Routine(
            name='oddball_trial',
            components=[circle_stim, key_resp_oddball],
        )
        oddball_trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        circle_stim.setFillColor(color)
        circle_stim.setLineColor(color)
        # create starting attributes for key_resp_oddball
        key_resp_oddball.keys = []
        key_resp_oddball.rt = []
        _key_resp_oddball_allKeys = []
        # store start times for oddball_trial
        oddball_trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        oddball_trial.tStart = globalClock.getTime(format='float')
        oddball_trial.status = STARTED
        thisExp.addData('oddball_trial.started', oddball_trial.tStart)
        oddball_trial.maxDuration = None
        # keep track of which components have finished
        oddball_trialComponents = oddball_trial.components
        for thisComponent in oddball_trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "oddball_trial" ---
        thisExp.currentRoutine = oddball_trial
        oddball_trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # if trial has changed, end Routine now
            if hasattr(thisOddball_loop, 'status') and thisOddball_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *circle_stim* updates
            
            # if circle_stim is starting this frame...
            if circle_stim.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                circle_stim.frameNStart = frameN  # exact frame index
                circle_stim.tStart = t  # local t and not account for scr refresh
                circle_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle_stim.started')
                # update status
                circle_stim.status = STARTED
                circle_stim.setAutoDraw(True)
            
            # if circle_stim is active this frame...
            if circle_stim.status == STARTED:
                # update params
                pass
            
            # if circle_stim is stopping this frame...
            if circle_stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_stim.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_stim.tStop = t  # not accounting for scr refresh
                    circle_stim.tStopRefresh = tThisFlipGlobal  # on global time
                    circle_stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'circle_stim.stopped')
                    # update status
                    circle_stim.status = FINISHED
                    circle_stim.setAutoDraw(False)
            
            # *key_resp_oddball* updates
            waitOnFlip = False
            
            # if key_resp_oddball is starting this frame...
            if key_resp_oddball.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_oddball.frameNStart = frameN  # exact frame index
                key_resp_oddball.tStart = t  # local t and not account for scr refresh
                key_resp_oddball.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_oddball, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_oddball.started')
                # update status
                key_resp_oddball.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_oddball.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_oddball.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_oddball is stopping this frame...
            if key_resp_oddball.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_oddball.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_oddball.tStop = t  # not accounting for scr refresh
                    key_resp_oddball.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp_oddball.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_oddball.stopped')
                    # update status
                    key_resp_oddball.status = FINISHED
                    key_resp_oddball.status = FINISHED
            if key_resp_oddball.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_oddball.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_oddball_allKeys.extend(theseKeys)
                if len(_key_resp_oddball_allKeys):
                    key_resp_oddball.keys = _key_resp_oddball_allKeys[-1].name  # just the last key pressed
                    key_resp_oddball.rt = _key_resp_oddball_allKeys[-1].rt
                    key_resp_oddball.duration = _key_resp_oddball_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_oddball.keys == str(correct_key)) or (key_resp_oddball.keys == correct_key):
                        key_resp_oddball.corr = 1
                    else:
                        key_resp_oddball.corr = 0
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=oddball_trial,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                oddball_trial.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if oddball_trial.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in oddball_trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "oddball_trial" ---
        for thisComponent in oddball_trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for oddball_trial
        oddball_trial.tStop = globalClock.getTime(format='float')
        oddball_trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('oddball_trial.stopped', oddball_trial.tStop)
        # check responses
        if key_resp_oddball.keys in ['', [], None]:  # No response was made
            key_resp_oddball.keys = None
            # was no response the correct answer?!
            if str(correct_key).lower() == 'none':
               key_resp_oddball.corr = 1;  # correct non-response
            else:
               key_resp_oddball.corr = 0;  # failed to respond (incorrectly)
        # store data for oddball_loop (TrialHandler)
        oddball_loop.addData('key_resp_oddball.keys',key_resp_oddball.keys)
        oddball_loop.addData('key_resp_oddball.corr', key_resp_oddball.corr)
        if key_resp_oddball.keys != None:  # we had a response
            oddball_loop.addData('key_resp_oddball.rt', key_resp_oddball.rt)
            oddball_loop.addData('key_resp_oddball.duration', key_resp_oddball.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if oddball_trial.maxDurationReached:
            routineTimer.addTime(-oddball_trial.maxDuration)
        elif oddball_trial.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "ITI" ---
        # create an object to store info about Routine ITI
        ITI = data.Routine(
            name='ITI',
            components=[text],
        )
        ITI.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ITI
        ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ITI.tStart = globalClock.getTime(format='float')
        ITI.status = STARTED
        thisExp.addData('ITI.started', ITI.tStart)
        ITI.maxDuration = None
        # keep track of which components have finished
        ITIComponents = ITI.components
        for thisComponent in ITI.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ITI" ---
        thisExp.currentRoutine = ITI
        ITI.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisOddball_loop, 'status') and thisOddball_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=ITI,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                ITI.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if ITI.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in ITI.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ITI
        ITI.tStop = globalClock.getTime(format='float')
        ITI.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ITI.stopped', ITI.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ITI.maxDurationReached:
            routineTimer.addTime(-ITI.maxDuration)
        elif ITI.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisOddball_loop as finished
        if hasattr(thisOddball_loop, 'status'):
            thisOddball_loop.status = FINISHED
        # if awaiting a pause, pause now
        if oddball_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            oddball_loop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'oddball_loop'
    oddball_loop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
