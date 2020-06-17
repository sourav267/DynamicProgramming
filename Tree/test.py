d=dict({
  "frame_id": 1,
  "group_info": [
    {
      "person_id": 1,
      "loc_x": 874,
      "loc_y": 227,
      "box": [
        839,
        103,
        70,
        248
      ],
      "contacts": [
        {
          "x": 929,
          "y": 244,
          "dist": 57.56735185849702
        }
      ]
    },
    {
      "person_id": 2,
      "loc_x": 929,
      "loc_y": 244,
      "box": [
        891,
        139,
        76,
        209
      ],
      "contacts": [
        {
          "x": 874,
          "y": 227,
          "dist": 57.56735185849702
        },
        {
          "x": 1023,
          "y": 248,
          "dist": 94.08506789071261
        }
      ]
    },
    {
      "person_id": 3,
      "loc_x": 1023,
      "loc_y": 248,
      "box": [
        981,
        140,
        84,
        215
      ],
      "contacts": [
        {
          "x": 929,
          "y": 244,
          "dist": 94.08506789071261
        }
      ]
    },
    {
      "person_id": 4,
      "loc_x": 1165,
      "loc_y": 455,
      "box": [
        1078,
        294,
        174,
        322
      ],
      "contacts": []
    },
    {
      "person_id": 5,
      "loc_x": 772,
      "loc_y": 117,
      "box": [
        746,
        45,
        51,
        143
      ],
      "contacts": []
    }
  ],
  "cluster_info": [
    {
      "cluster_id": 1,
      "cluster": [
        {
          "x": 929,
          "y": 244,
          "id": 1
        },
        {
          "x": 874,
          "y": 227,
          "id": 2
        },
        {
          "x": 1023,
          "y": 248,
          "id": 3
        }
      ]
    }
  ]
})
# print(len(d['group_info']))
print(len(d['cluster_info']))