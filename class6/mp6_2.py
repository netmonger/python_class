#!/usr/bin/env python

def conf_to_dict(a_list):
	a_dict = {}
	for x,elem in enumerate(a_list):
		a_dict[x] = elem
	return a_dict
