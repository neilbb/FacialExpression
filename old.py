function demo(eval, pot, act)
  {

    if (botGive === 1){
      move = "give two";
    }
    if (botGive === 0){
      move = "take one";
    }

    
    prompt = "";
    firsthalf = "";

    var lipsmile;
    var lipsmileval;
    var browin;
    var browinval;
    var browout;
    var browoutval;
    var purse;
    var purseval;

    var lippulldown;
    var lippulldownval;
    var nosedisgust;
    var nosedisgustval;
    var lippullup;
    var lippullupval;
    var anger;
    var angerval;

    var topeyelid;
    var topeyelidval;
    var bottomeyelid;
    var bottomeyelidval;
    var tense;
    var tenseval;
    var blink;
    var blinkval;
    var surprise;
    var surpriseval;
    var pout;
    var poutval;

    console.log(prompt);
    console.log("eval, pot, act are below: ");
    console.log(eval);
    console.log(pot);
    console.log(act);
  
   if(eval<0){ //DONE
      console.log("evaluation is negative");
      var tempeval = eval*-1;
      purse = "<purse=";
      purseval = transformation(0,4,0,150,tempeval); // swap the sign so it converts properly
      purse = purse + purseval + ">";
      firsthalf = firsthalf + purse;
      // added this condition so account for angry epa val -----------
      if(pot<0){
        if (eval<pot){
          if(pot > -0.95 && eval > -1.5){
          anger= "<anger=";
          angerval = transformation(0,4,0,110,tempeval);
          anger = anger + angerval + ">";
          firsthalf = firsthalf + anger;

          nosedisgust = "<nose_disgust=";
          nosedisgustval = transformation(0,4,0,50,tempeval);
          nosedisgust = nosedisgust + nosedisgustval + ">";
          firsthalf = firsthalf + nosedisgust;
         }
         
      }
      }
      //---------------------------------------------------------------
    }
    if(eval>0){ //DONE?
      //console.log("evaluation is positive");
      //<lip_smile> ---------------------------------
      lipsmile = "<lip_smile=";
      //smile 0-110
      lipsmileval = transformation(0,4,0,130,eval);
      lipsmile = lipsmile + lipsmileval + ">";
      firsthalf = firsthalf + lipsmile;
      //----------------------------------------------
      if(pot>2){
        browin = "<brow_in_up=";
        browinval = transformation(0,4,0,70,eval);
        browin = browin + browinval +  ">";
        firsthalf = firsthalf + browin;
        browout = "<brow_out_up=";
        browoutval = transformation(0,4,0,70,eval);
        browout = browout + browoutval + ">";
        firsthalf = firsthalf + browout;
      }
      else if (pot>0 && pot<2){
        browin = "<brow_in_up=";
        browinval = transformation(0,4,0,110,eval);
        browin = browin + browinval +  ">";
        firsthalf = firsthalf + browin;
        browout = "<brow_out_up=";
        browoutval = transformation(0,4,0,80,eval);
        browout = browout + browoutval + ">";
        firsthalf = firsthalf + browout;
      }
    }

    if(pot<0){ //DONE
      //console.log("potency is negative");
      lippulldown = "<lip_pull_down=";
      var temppot = pot * -1;
      lippulldownval = transformation(0,4,0,110,temppot);
      lippulldown = lippulldown + lippulldownval + ">";
      firsthalf = firsthalf + lippulldown;

      browin = "<brow_in_up=";
      browinval = transformation(0,4,0,120,temppot);
      browin = browin + browinval + ">";
      firsthalf = firsthalf + browin;
    }

    if (pot>0){ //DONE
      lippullup = "<lip_pull_up=";
      lippullupval = transformation(0,4,0,80,pot);
      lippullup = lippullup + lippullupval + ">";
      firsthalf = firsthalf + lippullup;

      nosedisgust = "<nose_disgust=";
      nosedisgustval = transformation(0,4,0,70,pot);
      nosedisgust = nosedisgust + nosedisgustval + ">";
      firsthalf = firsthalf + nosedisgust;

      if (eval<0 && act>2){
      // Anger is higher if activity is higher
      anger = "<anger=";
      angerval = transformation(0,4,0,110,pot);
      anger = anger + angerval + ">";
      firsthalf = firsthalf + anger;
      }
      else if(eval<0 && act>0 && act<2){
      anger = "<anger=";
      angerval = transformation(0,4,0,95,pot);
      anger = anger + angerval + ">";
      firsthalf = firsthalf + anger;
      }
    }

    if(act<0){ //DONE
      //console.log("activity is negative");
      var tempact = act * -1;
      topeyelid = "<top_eyelid=";
      topeyelidval = transformation(0,4,0,20,tempact);
      topeyelid = topeyelid + topeyelidval + ">";
      firsthalf = firsthalf + topeyelid;

      bottomeyelid = "<bottom_eyelid=";
      bottomeyelidval = transformation(0,4,0,100,tempact);
      bottomeyelid = bottomeyelid + bottomeyelidval + ">"
      firsthalf = firsthalf + bottomeyelid;

      if (pot < 0){
        tense = "<tense=";
        tenseval = transformation(0,4,0,90,tempact);
        tense = tense + tenseval + ">";
        firsthalf = firsthalf + tense;
      }
    }

    if (act>0){ //DONE
      blink = "<blink>";
      firsthalf = firsthalf + blink;
      if (act>1){ // changed to 1
        surprise = "<surprise=";
        surpriseval = transformation(0,4,0,120,act);
        surprise = surprise + surpriseval + ">";
        firsthalf = firsthalf + surprise;
        pout = "<pout=";
        poutval = transformation(0,4,0,120,act);
        pout = pout + poutval + ">";
        firsthalf = firsthalf + pout;
      }
    }
    console.log(firsthalf);
    prompt = firsthalf + "I feel " + firsthalf + feeling + firsthalf;
    console.log(prompt);
    howToSendText('animate2','google',prompt);  
  } //close demo function
