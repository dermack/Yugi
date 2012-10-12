unit UMain;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, dxSkinsCore, dxSkinBlack, dxSkinBlue, dxSkinCaramel, dxSkinCoffee,
  dxSkinDarkRoom, dxSkinDarkSide, dxSkinFoggy, dxSkinGlassOceans,
  dxSkiniMaginary, dxSkinLilian, dxSkinLiquidSky, dxSkinLondonLiquidSky,
  dxSkinMcSkin, dxSkinMoneyTwins, dxSkinOffice2007Black, dxSkinOffice2007Blue,
  dxSkinOffice2007Green, dxSkinOffice2007Pink, dxSkinOffice2007Silver,
  dxSkinOffice2010Black, dxSkinOffice2010Blue, dxSkinOffice2010Silver,
  dxSkinPumpkin, dxSkinSeven, dxSkinSharp, dxSkinSilver, dxSkinSpringTime,
  dxSkinStardust, dxSkinSummer2008, dxSkinsDefaultPainters, dxSkinValentine,
  dxSkinXmas2008Blue, cxLookAndFeels, dxSkinsForm, cxGraphics,
  cxLookAndFeelPainters, Menus, StdCtrls, cxButtons;

type
  TfrmMain = class(TForm)
    SkinController: TdxSkinController;
    btnCadastroCarta: TcxButton;
    btnEditarDeck: TcxButton;
    btnJogar: TcxButton;
    procedure btnEditarDeckClick(Sender: TObject);
    procedure btnCadastroCartaClick(Sender: TObject);
    procedure FormShow(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
    userID: integer;
  end;

var
  frmMain: TfrmMain;

implementation

uses UCadastroCarta, UDeckEdit, ULogin;

{$R *.dfm}

procedure TfrmMain.btnCadastroCartaClick(Sender: TObject);
begin
   if not Assigned(frmCadastroCarta) then
      frmCadastroCarta := TfrmCadastroCarta.Create(self);

   frmCadastroCarta.ShowModal;
   FreeAndNil(frmCadastroCarta);
end;

procedure TfrmMain.btnEditarDeckClick(Sender: TObject);
begin
   if not Assigned(frmDeckEdit) then
      frmDeckEdit := TfrmDeckEdit.Create(self);

   frmDeckEdit.ShowModal;
   FreeAndNil(frmDeckEdit);

end;

procedure TfrmMain.FormShow(Sender: TObject);
begin
   if not Assigned(frmLogin) then
      frmLogin := TfrmLogin.Create(self);

   if not (frmLogin.ShowModal = mrOk) then
        Application.Terminate;

end;

end.
