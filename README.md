# simple-fetch-py-server

#### Simple python fetch server that parses data.json file and returns parsed data as response to GET-request with time period in params.

This server was deployed on http://mikhailmoro.pythonanywhere.com

_This server can be uses with my android app (https://github.com/mikhail-moro/simple-classes-shedule-android-app)._


### Request

Server accepts GET-requests with two params that contains data of time period of classes.

Example for local server:
```
  http://localhost:3000/?start_time=2022-09-01T00:00:00&end_time=2022-10-30T00:00:00
```


Without code changing response will be contained .json with this structure:

```
  {
      ...,
  
      "yyyy-mm-dd": [
          ...,
    
          {
              "module": ...,
              "name": ...,
              "theme": ...,
              "type": ...,
              "aud": ...,
              "link": ...,
              "teachers": ...,
              "groups": ...,
              "startTime": ...,
              "endTime": ...,
              "color": ...,
          },
    
          ...
      ],
  
      ...
  }
```

### Data

File data.json contains the data of my classes at September and October.

Without code changing structure of data.json shoud be an array and contains this keys:
```
    [
        ...,
        
        {
            "name": ...,
            "color": ...,
            "start": "yyyy-mm-ddThh:mm:ss+hh:mm",
            "end": "yyyy-mm-ddThh:mm:ss+hh:mm",
            "info": {
                "moduleName": ...,
                "theme": ...,
                "aud": ...,
                "link": ...,
                "teachersNames": ...,
                "groupName": ...,
                "type": ...,
            }
        },
    
        ...
    ]
```
