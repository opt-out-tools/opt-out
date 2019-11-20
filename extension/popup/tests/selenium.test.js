const {
  Builder, By, Key, until, Options,
} = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');


const XPI_PATH = './extension/';
const profile = new firefox.Profile();
profile.setAcceptUntrustedCerts(true);
profile.setAssumeUntrustedCertIssuer(false);
profile.setPreference('xpinstall.signatures.required', false);
profile.addExtension(XPI_PATH);

const firefoxOption = new firefox.Options();
firefoxOption.setProfile(profile);
// firefoxOption.setBinary('/usr/local/bin/firefox');
firefoxOption.setBinary('/opt/firefox_dev/firefox');

const rootURL = 'https://twitter.com/';

const d = new Builder()
  .forBrowser('firefox')
  .setFirefoxOptions(firefoxOption)
  .build();
const waitUntilTime = 20000;
let driver;

jest.setTimeout(30000);

async function getElementById(id) {
  const el = await driver.wait(until.elementLocated(By.id(id)), waitUntilTime);
  return await driver.wait(until.elementIsVisible(el), waitUntilTime);
}

async function getElementByXPath(xpath) {
  const el = await driver.wait(until.elementLocated(By.xpath(xpath)), waitUntilTime);
  return await driver.wait(until.elementIsVisible(el), waitUntilTime);
}


it('waits for the driver to start', () => d.then((_d) => { driver = _d; }));

it('initialises the context', async () => {
  await driver.manage().window().setPosition(0, 0);
  await driver.manage().window().setSize(1280, 1024);
  await driver.get(rootURL);
});

it('should click on navbar button to display a drawer', async () => {
  driver.findElement({ name: 'session[username_or_email]' }).sendKeys('mail.server.testic@gmail.com');
  driver.findElement({ name: 'session[password]' }).sendKeys('testing123');
  driver.sleep(2000);
  await getElementByXPath('/html/body/div[1]/div/div[1]/div[1]/div[1]/form/input[1]').then((res) => res.click());
  // await expect(el).toEqual(expected)
});
