import wx

class windowClass(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        self.Move((450,55))
        self.basicGUI()
        
    def basicGUI(self):

        #menu work
        panel = wx.Panel(self)        
        menuBar = wx.MenuBar()

        #user input
        nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome','Nic')

        if nameBox.ShowModal()==wx.ID_OK:
            userName = nameBox.GetValue()

        yesNoBox = wx.MessageDialog(None, 'Do you love me?', 'Choose', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()

        #button inits
        fileButton = wx.Menu()
        editButton = wx.Menu()
        helpButton = wx.Menu()
        
        #MENU sets
        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')
        menuBar.Append(helpButton, 'Help')

        #drop down buttons
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'status msg...')
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        noHelp = helpButton.Append(wx.ID_HELP, 'No one can help', 'heeeeeeelllllp')

       

        
        #MultiChoice
        chooseOneBox = wx.SingleChoiceDialog(None, 'What is your favorite color?',
                                             'Color',
                                             ['green', 'blue', 'red', 'orange'])
        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()

        #panel
        wx.TextCtrl(panel, pos=(3, 20), size=(378, 50))
        aweText = wx.StaticText(panel, -1, "Awesome Text        ", (3, 3))
        aweText.SetForegroundColour('#67cddc')
        aweText.SetBackgroundColour('black')
        rlyAweText = wx.StaticText(panel, -1, "Custom Awesome      ", (100, 3))
        rlyAweText.SetForegroundColour(favColor)
        rlyAweText.SetBackgroundColour('black')
        
        #attributes      
        extraTitle = ''
        if yesNoAnswer == wx.ID_NO:
            extraTitle = ', you Loser'
        #    userName = 'Loser!'
        self.SetTitle('Welcome '+userName+extraTitle)
        self.Show(True)


    def Quit(self,e):
        self.Close()
            
def main():
    app = wx.App()
    windowClass(None)
    app.MainLoop()

main()
