import json

game_data = {
    "enemies": [
        {
            "x": 450,
            "y": 400,
            "speed_walk": 6,
            "speed_run": 5,
            "gravity": 14,
            "jump_power": 30,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "jump_height": 140,
            "p_scale": 0.08,
            "interval_time_jump": 300
        },
        {
            "x":900,
            "y":400,
            "speed_walk":6,
            "speed_run":5,
            "gravity":14,
            "jump_power":30,
            "frame_rate_ms":150,
            "move_rate_ms":50,
            "jump_height":140,
            "p_scale":0.08,
            "interval_time_jump":300
        },
        {
            "x":1500,
            "y":400,
            "speed_walk":10,
            "speed_run":5,
            "gravity":14,
            "jump_power":30,
            "frame_rate_ms":150,
            "move_rate_ms":50,
            "jump_height":140,
            "p_scale":0.08,
            "interval_time_jump":300
        },
        {
            "x":4500,
            "y":400,
            "speed_walk":10,
            "speed_run":5,
            "gravity":14,
            "jump_power":30,
            "frame_rate_ms":150,
            "move_rate_ms":50,
            "jump_height":140,
            "p_scale":0.08,
            "interval_time_jump":300
        },
        {
            "x":2500,
            "y":400,
            "speed_walk":10,
            "speed_run":5,
            "gravity":14,
            "jump_power":30,
            "frame_rate_ms":150,
            "move_rate_ms":50,
            "jump_height":140,
            "p_scale":0.08,
            "interval_time_jump":300
        }
        
    ],
    "platforms": [
        {
            "x": 510,
            "y": 500,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": True,
            "type": 24
        },
        {
            "x": 600,
            "y": 430,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": False,
            "type": 25
        },
        {
            "x": 510,
            "y": 500,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": True,
            "type": 24
        },
         {
            "x": 600,
            "y": 430,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": True,
            "type": 24
        },
          {
            "x": 650,
            "y": 500,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": False,
            "type": 24
        },
           {
            "x": 510,
            "y": 500,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": True,
            "type": 24
        },
            {
            "x": 510,
            "y": 500,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": True,
            "type": 24
        },
             {
            "x": 510,
            "y": 500,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": True,
            "type": 24
        },
              {
            "x": 510,
            "y": 500,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": True,
            "type": 24
        },
               {
            "x": 510,
            "y": 500,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": True,
            "type": 24
        },
                {
            "x": 510,
            "y": 500,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": True,
            "type": 24
        },
                 {
            "x": 510,
            "y": 500,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": True,
            "type": 24
        },
                  {
            "x": 510,
            "y": 500,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": True,
            "type": 24
        },
                   {
            "x": 510,
            "y": 500,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": True,
            "type": 24
        },
                    {
            "x": 510,
            "y": 500,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": True,
            "type": 24
        },
    ],
    
     "items":[
        {
            "x": 510,
            "y": 500,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": True,
            "type": 24
        },
        {
            "x": 600,
            "y": 430,
            "width": 50,
            "height": 50,
            "frame_rate_ms": 150,
            "move_rate_ms": 50,
            "move": False,
            "type": 25
        },
     ]   
}

with open("game_data.json", "w") as file:
    json.dump(game_data, file)