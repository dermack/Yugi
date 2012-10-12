unit ULogin;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, DB, ADODB, cxGraphics, cxControls, cxLookAndFeels,
  cxLookAndFeelPainters, cxContainer, cxEdit, dxSkinsCore, dxSkinBlack,
  dxSkinBlue, dxSkinCaramel, dxSkinCoffee, dxSkinDarkRoom, dxSkinDarkSide,
  dxSkinFoggy, dxSkinGlassOceans, dxSkiniMaginary, dxSkinLilian,
  dxSkinLiquidSky, dxSkinLondonLiquidSky, dxSkinMcSkin, dxSkinMoneyTwins,
  dxSkinOffice2007Black, dxSkinOffice2007Blue, dxSkinOffice2007Green,
  dxSkinOffice2007Pink, dxSkinOffice2007Silver, dxSkinOffice2010Black,
  dxSkinOffice2010Blue, dxSkinOffice2010Silver, dxSkinPumpkin, dxSkinSeven,
  dxSkinSharp, dxSkinSilver, dxSkinSpringTime, dxSkinStardust, dxSkinSummer2008,
  dxSkinsDefaultPainters, dxSkinValentine, dxSkinXmas2008Blue, cxLabel,
  cxTextEdit, Menus, StdCtrls, cxButtons;

type
  TfrmLogin = class(TForm)
    qryLogin: TADOQuery;
    edtUser: TcxTextEdit;
    cxLabel1: TcxLabel;
    edtPass: TcxTextEdit;
    cxLabel2: TcxLabel;
    btnEntrar: TcxButton;
    btnSair: TcxButton;
    procedure btnEntrarClick(Sender: TObject);
    procedure btnSairClick(Sender: TObject);
    procedure edtUserKeyPress(Sender: TObject; var Key: Char);
    procedure edtPassKeyPress(Sender: TObject; var Key: Char);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmLogin: TfrmLogin;

implementation

uses UDataBase, UMain;

{$R *.dfm}

procedure TfrmLogin.btnEntrarClick(Sender: TObject);
begin
   {qryLogin.Active := False;
   qryLogin.SQL.Clear;
   qryLogin.SQL.Add('Select id FROM user WHERE username = :user');
   qryLogin.Parameters.ParamByName('user').Value := edtUser.Text;
   qryLogin.Active := True;

   if qryLogin.Eof then
   begin
      MessageDlg('Usu�rio Inv�lido', mtError, [mbOk], MB_ICONERROR);
      exit;
   end;}

   qryLogin.Active := False;
   qryLogin.SQL.Clear;
   qryLogin.SQL.Add('SELECT id FROM user WHERE username = :user AND passwd = PASSWORD(:pass)');
   qryLogin.Parameters.ParamByName('user').Value := edtUser.Text;
   qryLogin.Parameters.ParamByName('pass').Value := edtPass.Text;
   qryLogin.Active := True;


   if qryLogin.Eof then
   begin
      MessageDlg('Usu�rio ou Senha Inv�lida', mtError, [mbOk], MB_ICONERROR);
      exit;
   end;

   MessageDlg('Bem vindo ' + edtUser.Text + '!', mtInformation, [mbOK], 0);

   frmMain.userID := qryLogin.Fields[0].AsInteger;
   ModalResult := mrOk;
end;

procedure TfrmLogin.btnSairClick(Sender: TObject);
begin
   close;
end;

procedure TfrmLogin.edtPassKeyPress(Sender: TObject; var Key: Char);
begin
   if key = #13 then
      btnEntrar.Click;
end;

procedure TfrmLogin.edtUserKeyPress(Sender: TObject; var Key: Char);
begin
   if key = #13 then
      btnEntrar.Click;
end;

end.
