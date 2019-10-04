#!/usr/bin/env python3




template = """
  /location/country:
    get:
      description: Get the name and international code for a country.
      operationId: getCountry
      parameters:
        - name: name
          in: query
          schema:
            type: integer
          example: United States of America
        - name: code
          in: query
          schema:
            type: integer
          example: US
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                type: object
                properties:
                    name:
                      type: string
                    code:
                      type: string
              examples:
                '0':
                  value: |
                    {
                        "code": "US",
                        "name": "United States of America"
                     }
      security:
        - Digest: []
      x-code-samples:
        - lang: 'curl'
          source: |
            curl -X GET -H "Authorization: Digest `echo -n $api_key|base64`" "https://api.example.com/v1/location/country/?code=US"
        - lang: 'python'
          source: |
            import requests
            import base64
            headers = {
              "Authorization": "Digest {}".format(
                base64.b64encode(api_key.encode("utf-8")).decode("utf-8")
              )
            }
            params = {
              "code": "US"
            }
            url = "https://api.example.com/v1/location/country"
            response = requests.get(url, headers=headers, params=params)
            print(response.json())
        - lang: JQuery
          source: |
            $.ajaxSetup({
              headers : {
                'Authorization' : 'Digest ' + btoa(api_key)
              }
            });
            url = "https://api.example.com/v1/location/country"
            params = {
              "code": "US"
            }
            $.getJSON(url, params)
            .done(function(json) {
              console.log(json)
            });
        - lang: PHP
          source: |
            $params = array(
              "code" => "US"
            );
            $url = "https://api.example.com/v1/location/country";
            $curl = curl_init();
            curl_setopt($curl, CURLOPT_URL, $url . "?" . http_build_query($params));
            curl_setopt($curl, CURLOPT_HTTPHEADER, array(
              'Authorization: Digest ' . base64_encode($api_key),
            ));
            $result = curl_exec($curl);
            curl_close($curl);
            print_r($result);
"""
