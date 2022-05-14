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
* Is there [EMI](2020-10-12--13-31-39Z--emi.md) from outside sources?
* Is the signal from any of the pairs in the same cable interfering with another
	pair? Otherwise known as *split pair*.

## Cable testers

* Basic ones only test [continuity](2020-10-19--13-22-22Z--continuity.md).
* Better testers can run a [wiremap](2020-10-19--13-23-15Z--wiremap.md) test.
  + Typically called a TDR.
    - **TDR:** [Time Domain Reflectometer](2020-10-19--14-16-02Z--tdr.md)
* Very expensive ones test [crosstalk](2020-10-19--13-26-24Z--crosstalk.md)
  + Can test for NEXT and FEXT
    - **NEXT:** Near End Crosstalk
    - **FEXT:** Far End Crosstalk
* As signal progresses it can [attenuate](2020-10-19--13-30-04Z--attenuate.md)
  + Siganl loss detected in decibal (dB)
  + Requires use of expensive *Cable Certifiers*.
