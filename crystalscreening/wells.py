#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dennisbrookner
"""
import pandas as pd


def well(screen, tray, well, quality, old_df=None, **kwargs):
    
    # to-do: check whether 'row' and 'column' are present in the tray dictionary, and if so, use that
    df = pd.DataFrame(columns = [screen['row']] + [screen['col']] 
                      + ['quality'] 
                      + list(screen[tray]['traystatics'].keys())
                      + list(screen['screenstatics'].keys())
                      + ['tray'] + ['well'])
    
    if type(well) == str:
        well = [well]
        
    if type(well) != list:
        raise TypeError('Improper type for well name')
    
    for w in well:
                
        df.loc[len(df.index)] = ([screen[tray][w[0]]] + [screen[tray][w[1]]]
                                 + [quality]
                                 + list(screen[tray]['traystatics'].values())
                                 + list(screen['screenstatics'].values())
                                 + [tray] + [w])
    
    if kwargs is not None:
        for key, value in kwargs.items():
            df[key] = value
    
    if old_df is not None:
        df = pd.concat([old_df, df], axis=0, ignore_index=True)
        #df = old_df.append(df)
        
    return df


def main():
    
    from crystalscreening.examples.samplescreens import screen1 as screen
    
    df = well(screen, 'tray1', 'A2', 'good', note='newly appeared')
    df = well(screen, 'tray2', ['A1', 'A2', 'A3'], 'needles', old_df=df, note = 'not mountable yet')
    df = well(screen, 'tray3', 'G2', 'needles', old_df=df)
    print(df)

if __name__ == '__main__': main()
