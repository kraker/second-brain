---
title: Testing copper cable runs
date: 2020-10-19 13:18:11
---

## Copper Challenges

* How long is the cable?
* Are any of the wires broken or is there a bad crimp?
* Is there a short? (2 bare wires touch)
* If there is a break, where is it?
* Are all wires terminated in the right place in the plug/jack?
* Is there [EMI](20201012133139-emi.md) from outside sources?
* Is the signal from any of the pairs in the same cable interfering with another
	pair? Otherwise known as *split pair*.

## Cable testers

* Basic ones only test [continuity](20201019132222-continuity.md).
* Better testers can run a [wiremap](20201019132315-wiremap.md) test.
  + Typically called a TDR.
    - **TDR:** [Time Domain Reflectometer](20201019141602-tdr.md)
* Very expensive ones test [crosstalk](20201019132624-crosstalk.md)
  + Can test for NEXT and FEXT
    - **NEXT:** Near End Crosstalk
    - **FEXT:** Far End Crosstalk
* As signal progresses it can [attenuate](20201019133004-attenuate.md)
  + Siganl loss detected in decibal (dB)
  + Requires use of expensive *Cable Certifiers*.
