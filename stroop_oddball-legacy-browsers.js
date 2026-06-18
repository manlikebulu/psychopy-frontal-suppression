/*********************** 
 * Stroop_Oddball *
 ***********************/


// store info about the experiment session:
let expName = 'stroop_oddball';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(stroop_InstructionRoutineBegin());
flowScheduler.add(stroop_InstructionRoutineEachFrame());
flowScheduler.add(stroop_InstructionRoutineEnd());
const stroop_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(stroop_loopLoopBegin(stroop_loopLoopScheduler));
flowScheduler.add(stroop_loopLoopScheduler);
flowScheduler.add(stroop_loopLoopEnd);



flowScheduler.add(oddball_instructionRoutineBegin());
flowScheduler.add(oddball_instructionRoutineEachFrame());
flowScheduler.add(oddball_instructionRoutineEnd());
const oddball_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(oddball_loopLoopBegin(oddball_loopLoopScheduler));
flowScheduler.add(oddball_loopLoopScheduler);
flowScheduler.add(oddball_loopLoopEnd);



flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'stroop_conditions.xlsx', 'path': 'stroop_conditions.xlsx'},
    {'name': 'oddball_conditions.xlsx', 'path': 'oddball_conditions.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2026.1.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var stroop_InstructionClock;
var instructionStroop;
var confirm_resp;
var stroop_trialClock;
var fixation;
var stroop_stim;
var key_resp_stroop;
var ITIClock;
var text;
var oddball_instructionClock;
var instructionOddball;
var confirm_key_resp;
var oddball_trialClock;
var oddball_fixation;
var circle_stim;
var key_resp_oddball;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "stroop_Instruction"
  stroop_InstructionClock = new util.Clock();
  instructionStroop = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructionStroop',
    text: 'You are about to start a Stroop task. This task will last 6 minutes.\n\nIn each trial, a word will appear in a colored ink. Your task is to respond to the colour of the ink, not the meaning of the word.\n\nUse the following keys:\nR = Red, Y = Yellow, G = Green and B = Blue\n\nRemember:\n\nRespond to the COLOUR , not the word\nStay fast and accurate\n\nPress SPACE to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  confirm_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "stroop_trial"
  stroop_trialClock = new util.Clock();
  fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  stroop_stim = new visual.TextStim({
    win: psychoJS.window,
    name: 'stroop_stim',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_stroop = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ITI"
  ITIClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "oddball_instruction"
  oddball_instructionClock = new util.Clock();
  instructionOddball = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructionOddball',
    text: 'WELCOME\n\nIn this task, you will see a series of circles appear one at a time.\n\nMost of the circles will be BLACK, while a few will be RED.\n\nYOUR TASK:\n- Press the SPACEBAR as quickly and accurately as possible ONLY when you see a RED circle.\n- Do NOT press any key when you see a BLACK circle.\n\nRespond as fast as you can while staying accurate.\n\nFocus on the screen at all times, as the circles will appear quickly and in random order.\n\nPress SPACEBAR to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  confirm_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "oddball_trial"
  oddball_trialClock = new util.Clock();
  oddball_fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'oddball_fixation',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  circle_stim = new visual.Polygon({
    win: psychoJS.window, name: 'circle_stim', 
    edges: 100, size:[0.5, 0.5],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -1, 
    interpolate: true, 
  });
  
  key_resp_oddball = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var stroop_InstructionMaxDurationReached;
var _confirm_resp_allKeys;
var stroop_InstructionMaxDuration;
var stroop_InstructionComponents;
function stroop_InstructionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stroop_Instruction' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    stroop_InstructionClock.reset();
    routineTimer.reset();
    stroop_InstructionMaxDurationReached = false;
    // update component parameters for each repeat
    confirm_resp.keys = undefined;
    confirm_resp.rt = undefined;
    _confirm_resp_allKeys = [];
    psychoJS.experiment.addData('stroop_Instruction.started', globalClock.getTime());
    stroop_InstructionMaxDuration = null
    // keep track of which components have finished
    stroop_InstructionComponents = [];
    stroop_InstructionComponents.push(instructionStroop);
    stroop_InstructionComponents.push(confirm_resp);
    
    stroop_InstructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function stroop_InstructionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stroop_Instruction' ---
    // get current time
    t = stroop_InstructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructionStroop* updates
    if (t >= 0.0 && instructionStroop.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructionStroop.tStart = t;  // (not accounting for frame time here)
      instructionStroop.frameNStart = frameN;  // exact frame index
      
      instructionStroop.setAutoDraw(true);
    }
    
    
    // if instructionStroop is active this frame...
    if (instructionStroop.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *confirm_resp* updates
    if (t >= 0.0 && confirm_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirm_resp.tStart = t;  // (not accounting for frame time here)
      confirm_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { confirm_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { confirm_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { confirm_resp.clearEvents(); });
    }
    
    // if confirm_resp is active this frame...
    if (confirm_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = confirm_resp.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _confirm_resp_allKeys = _confirm_resp_allKeys.concat(theseKeys);
      if (_confirm_resp_allKeys.length > 0) {
        confirm_resp.keys = _confirm_resp_allKeys[_confirm_resp_allKeys.length - 1].name;  // just the last key pressed
        confirm_resp.rt = _confirm_resp_allKeys[_confirm_resp_allKeys.length - 1].rt;
        confirm_resp.duration = _confirm_resp_allKeys[_confirm_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    stroop_InstructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stroop_InstructionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stroop_Instruction' ---
    stroop_InstructionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('stroop_Instruction.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(confirm_resp.corr, level);
    }
    psychoJS.experiment.addData('confirm_resp.keys', confirm_resp.keys);
    if (typeof confirm_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('confirm_resp.rt', confirm_resp.rt);
        psychoJS.experiment.addData('confirm_resp.duration', confirm_resp.duration);
        routineTimer.reset();
        }
    
    confirm_resp.stop();
    // the Routine "stroop_Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var stroop_loop;
function stroop_loopLoopBegin(stroop_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    stroop_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stroop_conditions.xlsx',
      seed: undefined, name: 'stroop_loop'
    });
    psychoJS.experiment.addLoop(stroop_loop); // add the loop to the experiment
    currentLoop = stroop_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    stroop_loop.forEach(function() {
      snapshot = stroop_loop.getSnapshot();
    
      stroop_loopLoopScheduler.add(importConditions(snapshot));
      stroop_loopLoopScheduler.add(stroop_trialRoutineBegin(snapshot));
      stroop_loopLoopScheduler.add(stroop_trialRoutineEachFrame());
      stroop_loopLoopScheduler.add(stroop_trialRoutineEnd(snapshot));
      stroop_loopLoopScheduler.add(ITIRoutineBegin(snapshot));
      stroop_loopLoopScheduler.add(ITIRoutineEachFrame());
      stroop_loopLoopScheduler.add(ITIRoutineEnd(snapshot));
      stroop_loopLoopScheduler.add(stroop_loopLoopEndIteration(stroop_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function stroop_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(stroop_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function stroop_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var oddball_loop;
function oddball_loopLoopBegin(oddball_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    oddball_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'oddball_conditions.xlsx',
      seed: undefined, name: 'oddball_loop'
    });
    psychoJS.experiment.addLoop(oddball_loop); // add the loop to the experiment
    currentLoop = oddball_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    oddball_loop.forEach(function() {
      snapshot = oddball_loop.getSnapshot();
    
      oddball_loopLoopScheduler.add(importConditions(snapshot));
      oddball_loopLoopScheduler.add(oddball_trialRoutineBegin(snapshot));
      oddball_loopLoopScheduler.add(oddball_trialRoutineEachFrame());
      oddball_loopLoopScheduler.add(oddball_trialRoutineEnd(snapshot));
      oddball_loopLoopScheduler.add(ITIRoutineBegin(snapshot));
      oddball_loopLoopScheduler.add(ITIRoutineEachFrame());
      oddball_loopLoopScheduler.add(ITIRoutineEnd(snapshot));
      oddball_loopLoopScheduler.add(oddball_loopLoopEndIteration(oddball_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function oddball_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(oddball_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function oddball_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var stroop_trialMaxDurationReached;
var _key_resp_stroop_allKeys;
var stroop_trialMaxDuration;
var stroop_trialComponents;
function stroop_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stroop_trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    stroop_trialClock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    stroop_trialMaxDurationReached = false;
    // update component parameters for each repeat
    stroop_stim.setColor(new util.Color(color));
    stroop_stim.setText(word);
    key_resp_stroop.keys = undefined;
    key_resp_stroop.rt = undefined;
    _key_resp_stroop_allKeys = [];
    psychoJS.experiment.addData('stroop_trial.started', globalClock.getTime());
    stroop_trialMaxDuration = null
    // keep track of which components have finished
    stroop_trialComponents = [];
    stroop_trialComponents.push(fixation);
    stroop_trialComponents.push(stroop_stim);
    stroop_trialComponents.push(key_resp_stroop);
    
    stroop_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function stroop_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stroop_trial' ---
    // get current time
    t = stroop_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation* updates
    if (t >= 0.0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }
    
    
    // if fixation is active this frame...
    if (fixation.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      fixation.tStop = t;  // not accounting for scr refresh
      fixation.frameNStop = frameN;  // exact frame index
      // update status
      fixation.status = PsychoJS.Status.FINISHED;
      fixation.setAutoDraw(false);
    }
    
    
    // *stroop_stim* updates
    if (t >= 0.5 && stroop_stim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stroop_stim.tStart = t;  // (not accounting for frame time here)
      stroop_stim.frameNStart = frameN;  // exact frame index
      
      stroop_stim.setAutoDraw(true);
    }
    
    
    // if stroop_stim is active this frame...
    if (stroop_stim.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (stroop_stim.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      stroop_stim.tStop = t;  // not accounting for scr refresh
      stroop_stim.frameNStop = frameN;  // exact frame index
      // update status
      stroop_stim.status = PsychoJS.Status.FINISHED;
      stroop_stim.setAutoDraw(false);
    }
    
    
    // *key_resp_stroop* updates
    if (t >= 0.5 && key_resp_stroop.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_stroop.tStart = t;  // (not accounting for frame time here)
      key_resp_stroop.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_stroop.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_stroop.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_stroop.clearEvents(); });
    }
    frameRemains = 0.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (key_resp_stroop.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      key_resp_stroop.tStop = t;  // not accounting for scr refresh
      key_resp_stroop.frameNStop = frameN;  // exact frame index
      // update status
      key_resp_stroop.status = PsychoJS.Status.FINISHED;
      frameRemains = 0.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (key_resp_stroop.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        key_resp_stroop.tStop = t;  // not accounting for scr refresh
        key_resp_stroop.frameNStop = frameN;  // exact frame index
        // update status
        key_resp_stroop.status = PsychoJS.Status.FINISHED;
        key_resp_stroop.status = PsychoJS.Status.FINISHED;
          }
        
      }
      
      // if key_resp_stroop is active this frame...
      if (key_resp_stroop.status === PsychoJS.Status.STARTED) {
        let theseKeys = key_resp_stroop.getKeys({
          keyList: typeof ['r','b','y','g'] === 'string' ? [['r','b','y','g']] : ['r','b','y','g'], 
          waitRelease: false
        });
        _key_resp_stroop_allKeys = _key_resp_stroop_allKeys.concat(theseKeys);
        if (_key_resp_stroop_allKeys.length > 0) {
          key_resp_stroop.keys = _key_resp_stroop_allKeys[_key_resp_stroop_allKeys.length - 1].name;  // just the last key pressed
          key_resp_stroop.rt = _key_resp_stroop_allKeys[_key_resp_stroop_allKeys.length - 1].rt;
          key_resp_stroop.duration = _key_resp_stroop_allKeys[_key_resp_stroop_allKeys.length - 1].duration;
          // was this correct?
          if (key_resp_stroop.keys == '') {
              key_resp_stroop.corr = 1;
          } else {
              key_resp_stroop.corr = 0;
          }
        }
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      stroop_trialComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function stroop_trialRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'stroop_trial' ---
      stroop_trialComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('stroop_trial.stopped', globalClock.getTime());
      // was no response the correct answer?!
      if (key_resp_stroop.keys === undefined) {
        if (['None','none',undefined].includes('')) {
           key_resp_stroop.corr = 1;  // correct non-response
        } else {
           key_resp_stroop.corr = 0;  // failed to respond (incorrectly)
        }
      }
      // store data for current loop
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(key_resp_stroop.corr, level);
      }
      psychoJS.experiment.addData('key_resp_stroop.keys', key_resp_stroop.keys);
      psychoJS.experiment.addData('key_resp_stroop.corr', key_resp_stroop.corr);
      if (typeof key_resp_stroop.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('key_resp_stroop.rt', key_resp_stroop.rt);
          psychoJS.experiment.addData('key_resp_stroop.duration', key_resp_stroop.duration);
          }
      
      key_resp_stroop.stop();
      if (routineForceEnded) {
          routineTimer.reset();} else if (stroop_trialMaxDurationReached) {
          stroop_trialClock.add(stroop_trialMaxDuration);
      } else {
          stroop_trialClock.add(2.000000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var ITIMaxDurationReached;
var ITIMaxDuration;
var ITIComponents;
function ITIRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'ITI' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      ITIClock.reset(routineTimer.getTime());
      routineTimer.add(1.000000);
      ITIMaxDurationReached = false;
      // update component parameters for each repeat
      psychoJS.experiment.addData('ITI.started', globalClock.getTime());
      ITIMaxDuration = null
      // keep track of which components have finished
      ITIComponents = [];
      ITIComponents.push(text);
      
      ITIComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function ITIRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'ITI' ---
      // get current time
      t = ITIClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *text* updates
      if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        text.tStart = t;  // (not accounting for frame time here)
        text.frameNStart = frameN;  // exact frame index
        
        text.setAutoDraw(true);
      }
      
      
      // if text is active this frame...
      if (text.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        text.tStop = t;  // not accounting for scr refresh
        text.frameNStop = frameN;  // exact frame index
        // update status
        text.status = PsychoJS.Status.FINISHED;
        text.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      ITIComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function ITIRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'ITI' ---
      ITIComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('ITI.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (ITIMaxDurationReached) {
          ITIClock.add(ITIMaxDuration);
      } else {
          ITIClock.add(1.000000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var oddball_instructionMaxDurationReached;
var _confirm_key_resp_allKeys;
var oddball_instructionMaxDuration;
var oddball_instructionComponents;
function oddball_instructionRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'oddball_instruction' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      oddball_instructionClock.reset();
      routineTimer.reset();
      oddball_instructionMaxDurationReached = false;
      // update component parameters for each repeat
      confirm_key_resp.keys = undefined;
      confirm_key_resp.rt = undefined;
      _confirm_key_resp_allKeys = [];
      psychoJS.experiment.addData('oddball_instruction.started', globalClock.getTime());
      oddball_instructionMaxDuration = null
      // keep track of which components have finished
      oddball_instructionComponents = [];
      oddball_instructionComponents.push(instructionOddball);
      oddball_instructionComponents.push(confirm_key_resp);
      
      oddball_instructionComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function oddball_instructionRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'oddball_instruction' ---
      // get current time
      t = oddball_instructionClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *instructionOddball* updates
      if (t >= 0.0 && instructionOddball.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        instructionOddball.tStart = t;  // (not accounting for frame time here)
        instructionOddball.frameNStart = frameN;  // exact frame index
        
        instructionOddball.setAutoDraw(true);
      }
      
      
      // if instructionOddball is active this frame...
      if (instructionOddball.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *confirm_key_resp* updates
      if (t >= 0.0 && confirm_key_resp.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        confirm_key_resp.tStart = t;  // (not accounting for frame time here)
        confirm_key_resp.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { confirm_key_resp.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { confirm_key_resp.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { confirm_key_resp.clearEvents(); });
      }
      
      // if confirm_key_resp is active this frame...
      if (confirm_key_resp.status === PsychoJS.Status.STARTED) {
        let theseKeys = confirm_key_resp.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _confirm_key_resp_allKeys = _confirm_key_resp_allKeys.concat(theseKeys);
        if (_confirm_key_resp_allKeys.length > 0) {
          confirm_key_resp.keys = _confirm_key_resp_allKeys[_confirm_key_resp_allKeys.length - 1].name;  // just the last key pressed
          confirm_key_resp.rt = _confirm_key_resp_allKeys[_confirm_key_resp_allKeys.length - 1].rt;
          confirm_key_resp.duration = _confirm_key_resp_allKeys[_confirm_key_resp_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      oddball_instructionComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function oddball_instructionRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'oddball_instruction' ---
      oddball_instructionComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('oddball_instruction.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(confirm_key_resp.corr, level);
      }
      psychoJS.experiment.addData('confirm_key_resp.keys', confirm_key_resp.keys);
      if (typeof confirm_key_resp.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('confirm_key_resp.rt', confirm_key_resp.rt);
          psychoJS.experiment.addData('confirm_key_resp.duration', confirm_key_resp.duration);
          routineTimer.reset();
          }
      
      confirm_key_resp.stop();
      // the Routine "oddball_instruction" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var oddball_trialMaxDurationReached;
var _key_resp_oddball_allKeys;
var oddball_trialMaxDuration;
var oddball_trialComponents;
function oddball_trialRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'oddball_trial' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      oddball_trialClock.reset(routineTimer.getTime());
      routineTimer.add(2.000000);
      oddball_trialMaxDurationReached = false;
      // update component parameters for each repeat
      circle_stim.setFillColor(new util.Color(color));
      circle_stim.setLineColor(new util.Color(color));
      key_resp_oddball.keys = undefined;
      key_resp_oddball.rt = undefined;
      _key_resp_oddball_allKeys = [];
      psychoJS.experiment.addData('oddball_trial.started', globalClock.getTime());
      oddball_trialMaxDuration = null
      // keep track of which components have finished
      oddball_trialComponents = [];
      oddball_trialComponents.push(oddball_fixation);
      oddball_trialComponents.push(circle_stim);
      oddball_trialComponents.push(key_resp_oddball);
      
      oddball_trialComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function oddball_trialRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'oddball_trial' ---
      // get current time
      t = oddball_trialClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *oddball_fixation* updates
      if (t >= 0.0 && oddball_fixation.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        oddball_fixation.tStart = t;  // (not accounting for frame time here)
        oddball_fixation.frameNStart = frameN;  // exact frame index
        
        oddball_fixation.setAutoDraw(true);
      }
      
      
      // if oddball_fixation is active this frame...
      if (oddball_fixation.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (oddball_fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        oddball_fixation.tStop = t;  // not accounting for scr refresh
        oddball_fixation.frameNStop = frameN;  // exact frame index
        // update status
        oddball_fixation.status = PsychoJS.Status.FINISHED;
        oddball_fixation.setAutoDraw(false);
      }
      
      
      // *circle_stim* updates
      if (t >= 0.5 && circle_stim.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        circle_stim.tStart = t;  // (not accounting for frame time here)
        circle_stim.frameNStart = frameN;  // exact frame index
        
        circle_stim.setAutoDraw(true);
      }
      
      
      // if circle_stim is active this frame...
      if (circle_stim.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (circle_stim.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        circle_stim.tStop = t;  // not accounting for scr refresh
        circle_stim.frameNStop = frameN;  // exact frame index
        // update status
        circle_stim.status = PsychoJS.Status.FINISHED;
        circle_stim.setAutoDraw(false);
      }
      
      
      // *key_resp_oddball* updates
      if (t >= 0.5 && key_resp_oddball.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        key_resp_oddball.tStart = t;  // (not accounting for frame time here)
        key_resp_oddball.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { key_resp_oddball.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { key_resp_oddball.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { key_resp_oddball.clearEvents(); });
      }
      frameRemains = 0.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (key_resp_oddball.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        key_resp_oddball.tStop = t;  // not accounting for scr refresh
        key_resp_oddball.frameNStop = frameN;  // exact frame index
        // update status
        key_resp_oddball.status = PsychoJS.Status.FINISHED;
        frameRemains = 0.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if (key_resp_oddball.status === PsychoJS.Status.STARTED && t >= frameRemains) {
          // keep track of stop time/frame for later
          key_resp_oddball.tStop = t;  // not accounting for scr refresh
          key_resp_oddball.frameNStop = frameN;  // exact frame index
          // update status
          key_resp_oddball.status = PsychoJS.Status.FINISHED;
          key_resp_oddball.status = PsychoJS.Status.FINISHED;
            }
          
        }
        
        // if key_resp_oddball is active this frame...
        if (key_resp_oddball.status === PsychoJS.Status.STARTED) {
          let theseKeys = key_resp_oddball.getKeys({
            keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
            waitRelease: false
          });
          _key_resp_oddball_allKeys = _key_resp_oddball_allKeys.concat(theseKeys);
          if (_key_resp_oddball_allKeys.length > 0) {
            key_resp_oddball.keys = _key_resp_oddball_allKeys[_key_resp_oddball_allKeys.length - 1].name;  // just the last key pressed
            key_resp_oddball.rt = _key_resp_oddball_allKeys[_key_resp_oddball_allKeys.length - 1].rt;
            key_resp_oddball.duration = _key_resp_oddball_allKeys[_key_resp_oddball_allKeys.length - 1].duration;
            // was this correct?
            if (key_resp_oddball.keys == correct_key) {
                key_resp_oddball.corr = 1;
            } else {
                key_resp_oddball.corr = 0;
            }
          }
        }
        
        // check for quit (typically the Esc key)
        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
        }
        
        // check if the Routine should terminate
        if (!continueRoutine) {  // a component has requested a forced-end of Routine
          routineForceEnded = true;
          return Scheduler.Event.NEXT;
        }
        
        continueRoutine = false;  // reverts to True if at least one component still running
        oddball_trialComponents.forEach( function(thisComponent) {
          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
            continueRoutine = true;
          }
        });
        
        // refresh the screen if continuing
        if (continueRoutine && routineTimer.getTime() > 0) {
          return Scheduler.Event.FLIP_REPEAT;
        } else {
          return Scheduler.Event.NEXT;
        }
      };
    }
    
    
function oddball_trialRoutineEnd(snapshot) {
      return async function () {
        //--- Ending Routine 'oddball_trial' ---
        oddball_trialComponents.forEach( function(thisComponent) {
          if (typeof thisComponent.setAutoDraw === 'function') {
            thisComponent.setAutoDraw(false);
          }
        });
        psychoJS.experiment.addData('oddball_trial.stopped', globalClock.getTime());
        // was no response the correct answer?!
        if (key_resp_oddball.keys === undefined) {
          if (['None','none',undefined].includes(correct_key)) {
             key_resp_oddball.corr = 1;  // correct non-response
          } else {
             key_resp_oddball.corr = 0;  // failed to respond (incorrectly)
          }
        }
        // store data for current loop
        // update the trial handler
        if (currentLoop instanceof MultiStairHandler) {
          currentLoop.addResponse(key_resp_oddball.corr, level);
        }
        psychoJS.experiment.addData('key_resp_oddball.keys', key_resp_oddball.keys);
        psychoJS.experiment.addData('key_resp_oddball.corr', key_resp_oddball.corr);
        if (typeof key_resp_oddball.keys !== 'undefined') {  // we had a response
            psychoJS.experiment.addData('key_resp_oddball.rt', key_resp_oddball.rt);
            psychoJS.experiment.addData('key_resp_oddball.duration', key_resp_oddball.duration);
            }
        
        key_resp_oddball.stop();
        if (routineForceEnded) {
            routineTimer.reset();} else if (oddball_trialMaxDurationReached) {
            oddball_trialClock.add(oddball_trialMaxDuration);
        } else {
            oddball_trialClock.add(2.000000);
        }
        // Routines running outside a loop should always advance the datafile row
        if (currentLoop === psychoJS.experiment) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        return Scheduler.Event.NEXT;
      }
    }
    
    
function importConditions(currentLoop) {
      return async function () {
        psychoJS.importAttributes(currentLoop.getCurrentTrial());
        return Scheduler.Event.NEXT;
        };
    }
    
    
async function quitPsychoJS(message, isCompleted) {
      // Check for and save orphaned data
      if (psychoJS.experiment.isEntryEmpty()) {
        psychoJS.experiment.nextEntry();
      }
      psychoJS.window.close();
      psychoJS.quit({message: message, isCompleted: isCompleted});
      
      return Scheduler.Event.QUIT;
    }
