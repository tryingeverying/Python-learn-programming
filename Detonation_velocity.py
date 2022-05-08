'def Eigenvalues(num_carbon,num_hydrogen,num_oxygen,num_nitrogen,production_enthalpy)':''
    molecular_weight=num_carbon*12+num_hydrogen+num_oxygen*16+num_nitrogen*14
'    if num_oxygen >= (2*num_carbon+num_hydrogen/2)':''
        N=(num_hydrogen+2*num_oxygen+2*num_nitrogen)/(4*molecular_weight)
        M=(4*molecular_weight)/(num_hydrogen+2*num_oxygen+2*num_nitrogen)
        Q=(28.9*num_hydrogen+94.05*num_carbon+0.239*production_enthalpy)/molecular_weight
'    elif  (2*num_carbon+num_hydrogen/2) > num_oxygen >= (num_hydrogen/2)':''
        N=(num_hydrogen+2*num_oxygen+2*num_nitrogen)/(4*molecular_weight)
        M=(56*num_nitrogen+88*num_oxygen-8*num_hydrogen)/(num_hydrogen+2*num_oxygen+2*num_nitrogen)
        Q=(28.9*num_hydrogen+94.05*(num_oxygen/2-num_hydrogen/4)+0.239*production_enthalpy)/molecular_weight
'    else':''
        N=(num_hydrogen+num_nitrogen)/(2*molecular_weight)
        M=(2*num_hydrogen+28*num_nitrogen+32*num_oxygen)/(num_hydrogen+num_nitrogen)
        Q=(57.8*num_oxygen+0.239*production_enthalpy)/molecular_weight
   
    eigenvalues=N*(M**(1/2))*((Q*1000)**(1/2))
    print(f"特征值为{eigenvalues}")
    return eigenvalues

'num_carbon=int(input('请输入分子中的碳原子个数':''))'
'num_hydrogen=int(input('请输入分子中的氢原子个数':''))'
'num_oxygen=int(input('请输入分子中的氧原子个数':''))'
'num_nitrogen=int(input('请输入分子中的氮原子个数':''))'
'density=float(input('请输入炸药的装药密度(g·cm-3)':''))'
'production_enthalpy=float(input('请输入炸药的标准摩尔生成焓(kJ·mol-1)':''))'

eigen_values=Eigenvalues(num_carbon,num_hydrogen,num_oxygen,num_nitrogen,production_enthalpy)
detonation_velocity=(1.01+1.313*density)*eigen_values**(1/2)
print(f'该化合物的爆速为{detonation_velocity}(km/s)')




















