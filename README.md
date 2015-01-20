<h1>Boolean_v1.0</h1>
<h2>Resume :</h2>
Boolean Program for Nastran Bulk File :
This program permit to removed GRID card in a Nastran Bulk file.

<b>Prerequisites :</b>
<ul> 
<li> Python 2.6.6 </li>
<li> Terminal (Mac OS, Linux) </li>
</ul> 

<p>With this program you can removed GRID card in a Nastran bulk file. 
In order to use this script you need :</p>
<ul>
<li>An original file containing all of bulk.</li>
<li>A file containing ID nodes in column to be deleted in the orginal file.</li>
</ul>

<h2>To Use the script :</h2>
<p> In order to use this script type <b>python</b> followed by the name of the script.</p>
```
$ python boolean.py
```
<p>It is possible to removed other card (FORCE, MOMENT, etc ...) by changing <b>Card_to_be_changed</b> variable into the script.</p>
