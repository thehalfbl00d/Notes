# Site Reliability Engineering

### Not ML based majorly

## Mitigation
Stop the bleeding.
- Proactive (predict)
- Reactive (Respone)


### Proactive
- Disaster Games -> Trying to break the system intentionally

### Reactive
- Monitoring
- Debugging


## Reliability

#### "three nines service"

- 99.9% reliable
- 8.9 unavailable for an year <- not good for a good product

#### "fine nine service"
- 99.999% reliable 
- 5 min unavailable for an year


### Solution
- Add more redundancy
     - have more servers
     - N + 1 for everything
     - send the state to other server if you dying, from the current server


