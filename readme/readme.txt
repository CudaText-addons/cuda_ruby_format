Plugin "Ruby Format" for CudaText.
It allows to format (beautify) source code for Ruby lexer.

If selection is made (only normal selection supported) then only selection is formatted, otherwise entire file is formatted. But note: selection formatting is incorrect in many cases, e.g. if you format only nested { } block, it will have incorrect indent regarding parent { } block.

Plugin has commands in menu "Plugins".
You can edit config file using two "Configure" commands:

    "Configure" opens config-file from "settings" folder, which is used when local file doesn't exist.
    "Configure (local)" opens config-file from the folder of current editor file. If local file doesn't exist, command suggests to copy global file into local name, and then opens it. 


Author: Alexey T.

3rd-party formatter: https://github.com/zmbacker/RubyFormat
Licensed under MIT license.
