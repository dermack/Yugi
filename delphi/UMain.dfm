object frmMain: TfrmMain
  Left = 0
  Top = 0
  Caption = 'Principal'
  ClientHeight = 352
  ClientWidth = 484
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  OnShow = FormShow
  PixelsPerInch = 96
  TextHeight = 13
  object btnCadastroCarta: TcxButton
    Left = 16
    Top = 296
    Width = 97
    Height = 25
    Caption = 'Cadastrar Carta'
    TabOrder = 0
    OnClick = btnCadastroCartaClick
  end
  object btnEditarDeck: TcxButton
    Left = 16
    Top = 23
    Width = 75
    Height = 25
    Caption = 'Editar Deck'
    TabOrder = 1
    OnClick = btnEditarDeckClick
  end
  object btnJogar: TcxButton
    Left = 192
    Top = 23
    Width = 75
    Height = 25
    Caption = 'Jogar'
    TabOrder = 2
  end
  object SkinController: TdxSkinController
    SkinName = 'Office2010Black'
    Left = 248
    Top = 120
  end
end
