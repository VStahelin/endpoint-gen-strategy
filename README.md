# endpoint-gen-strategy
Basically a simple URL shortening strategy for service integration with URL length limitation


Strategy:
- Get destination URL without parameters, save to database to avoid duplication
- Records the base path ID and parameters of this URL in a table and returns a UUID
- Concatenates base URL + /api + UUID

Receiving post:
- Get the UUID from the URL
- Redeem the corresponding Path from the db, additionally with prior params if applicable
- Forwards to the destination service

![image](https://github.com/VStahelin/endpoint-gen-strategy/assets/42194516/3fa4f7b1-af3d-45ff-85ac-94dbf31f5a0d)


